from ..arg_parser import Mode
from pydantic import BaseModel
from enum import Enum
from pathlib import Path
from typing import Optional, List

class DataConfig(BaseModel):
    raw_location: str
    clean_location: str
    batch_size: int
    seed: int
    

class TrainConfig(BaseModel):
    device: str
    epoch: int
    lr: float
    checkpoint_load_file: Optional[str]
    checkpoint_save_name: Optional[str]
    checkpoint_frequency: Optional[int]
    

class TestConfig(BaseModel):
    device: str
    checkpoint_load_file: Optional[str]
    batch_size: int
    plot_col_size: int
    plot_row_size: int
    plot_img_size: float
      

class Config(BaseModel):
    data: DataConfig
    train: TrainConfig
    test: TestConfig
    
    
class Shared(BaseModel):
    base_dir: Optional[Path]
    mode: Optional[Mode]
    # from config.yaml
    config: Config
    
    model_config = {
        "arbitrary_types_allowed": True
    }
    