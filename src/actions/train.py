from torch.utils.data import DataLoader
import pytorch_lightning as pl
from pytorch_lightning.loggers import CSVLogger
from pytorch_lightning.callbacks import ModelCheckpoint
from ..models import MLP, configure_optimizers, build_datasets, loss_function
from ..core.shared import shared

class PLWrapper(pl.LightningModule):
	def __init__(self):
		super().__init__()
		self.model = MLP((9, 64, 128, 256, 9))
		self.criterion = loss_function()


	def forward(self, x):
		x = self.model(x)
		return x
	

	def configure_optimizers(self):
		return configure_optimizers(model=self)
	

	def _shared_step(self, batch, stage):
		# batch consists of data and target
		if isinstance(batch, (list, tuple)):
			data, target = batch
		elif isinstance(batch, dict):
			# batch is a HuggingFace dictionary
			data = batch
			target = batch.get('labels')
		else:
			raise ValueError("Unknown batch format")

		# run the model
		if isinstance(data, dict):
			output = self.model(**data)
		else:
			output = self.model(data)

		# if model is calculating loss inside itself (like HF transformers)
		if hasattr(output, 'loss') and output.loss is not None:
			loss = output.loss
		else:
			# if output returns tuples (like RNNs) get the first element
			logits = output[0] if isinstance(output, tuple) else output
			loss = self.criterion(logits, target)

		self.log(f"{stage}_loss", loss, prog_bar=True, logger=True)
		return loss

	def training_step(self, batch, batch_idx):
		return self._shared_step(batch, "train")

	def validation_step(self, batch, batch_idx):
		return self._shared_step(batch, "val")



class UniversalDataModule(pl.LightningDataModule):
    def __init__(self):
        """
        Args:
            build_function: build_datasets function.
            cfg: All configuration (data path, batch_size, workers etc.)
        """
        super().__init__()
        self.builder_fn = build_datasets
        self.cfg = shared.config
        
        self.train_ds = None
        self.val_ds = None
        self.test_ds = None

    def setup(self, stage=None):
        datasets = self.builder_fn(self.cfg)
        
        self.train_ds = datasets.get("train")
        self.val_ds = datasets.get("val")
        self.test_ds = datasets.get("test")
        
        if not self.train_ds:
            raise ValueError("Train dataset is empty!")


    def train_dataloader(self):
        return DataLoader(
            self.train_ds,
            batch_size=self.cfg.data.batch_size,
            shuffle=True,
            num_workers=self.cfg.data.num_workers,
            pin_memory=True
        )


    def val_dataloader(self):
        if not self.val_ds: return None
        return DataLoader(
            self.val_ds,
            batch_size=self.cfg.data.batch_size,
            shuffle=False,
            num_workers=self.cfg.data.num_workers,
            pin_memory=True
        )


    def test_dataloader(self):
        if not self.test_ds: return None
        return DataLoader(
            self.test_ds,
            batch_size=self.cfg.data.batch_size,
            shuffle=False,
            num_workers=self.cfg.data.num_workers,
            pin_memory=True
        )
	


def start_training():
	save_name = shared.config.train.checkpoint_save_name
	logger = CSVLogger(
		save_dir=f"./outputs/{save_name}",
		name="", 
		version=""
		)


	checkpoint_callback = ModelCheckpoint(
		dirpath=f"./outputs/{save_name}/checkpoints",
		filename="{epoch:04d}",
		monitor=None,
		every_n_epochs=5,
		save_top_k=-1,
	)

	model = PLWrapper()

	trainer = pl.Trainer(
		max_epochs=shared.config.train.epoch,
		logger=logger,
		callbacks=[checkpoint_callback],
		log_every_n_steps=1
	)

	trainer.fit(model, datamodule=UniversalDataModule())
