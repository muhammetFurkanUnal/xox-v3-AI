from ..arg_parser import Mode
from pydantic import BaseModel
from enum import Enum
from pathlib import Path
from typing import Optional, List
from ...ai_models import AIModel

class DataConfig(BaseModel):
    batch_size: Optional[int]
    num_workers: Optional[int]
    seed: Optional[int]
    gather_save_folder: Optional[str]
    interim_save_folder: Optional[str]
    clean_save_folder: Optional[str]
    aug_save_folder: Optional[str]
    train_test_ratio: Optional[float]


class ModelConfig(BaseModel):
    model_folder_name: Optional[AIModel]
    

class TrainConfig(BaseModel):
    device: Optional[str]
    epoch: Optional[int]
    lr: Optional[float]
    dataset_load_file: Optional[str]
    checkpoint_load_file: Optional[str]
    checkpoint_save_name: Optional[str]
    checkpoint_frequency: Optional[int]
    

class TestConfig(BaseModel):
    device: Optional[str]
    checkpoint_load_file: Optional[str]
    batch_size: Optional[int]
      

class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
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
    