from enum import Enum


class AIModel(Enum):
	MLP = "MLP"


class AIModelProvider:
	def __init__(self, model:AIModel):
		self.ai_model:AIModel = model

	
	def get_architecture(self):
		if self.ai_model == AIModel.MLP:
			from .MLP import MLP
			return MLP
		

	def get_configure_optimizer(self):
		if self.ai_model == AIModel.MLP:
			from .MLP import configure_optimizers
			return configure_optimizers
		

	def get_data_module(self):
		if self.ai_model == AIModel.MLP:
			from .MLP import build_datasets
			return build_datasets
		

	def get_loss_function(self):
		if self.ai_model == AIModel.MLP:
			from .MLP import loss_function
			return loss_function()
		

	def get_dataset(self):
		if self.ai_model == AIModel.MLP:
			from .MLP import Humanishset
			return Humanishset
	