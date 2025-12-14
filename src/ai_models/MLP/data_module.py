
from torch.utils.data import Dataset, random_split, DataLoader
import torch
from ...core.shared import Config
from .dataset import Humanishset


def build_datasets(cfg:Config) -> dict:
    """
    Reads the data, processes and returns torch.util.data.Dataset objects.
    
    Returns:
        dict: {'train': Dataset, 'val': Dataset, 'test': Dataset (Optional)}
    """
    
    # Customizable code starts

    full_dataset = Humanishset(csv_path=cfg.train.dataset_load_file)
    
    train_size = int(cfg.data.train_test_ratio * len(full_dataset))
    val_size = len(full_dataset) - train_size
    
    generator = torch.Generator().manual_seed(42)
    train_ds, val_ds = random_split(full_dataset, [train_size, val_size], generator=generator)
    
    return {
        "train": train_ds,
        "val": val_ds,
        "test": None 
    }

    # Customizable code ends


