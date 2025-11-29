from .model import Shared, Config
from pathlib import Path
from typing import Optional
import yaml
from ..arg_parser import Args, args


def read_config_from_file(file_path:Path) -> Config:
	base_dir = Path(__file__).parent.parent.parent.parent
	cfg_dct = yaml.safe_load((base_dir/file_path).read_text())
	return Config(**cfg_dct)


def init_shared_res(args:Args) -> Shared:
    base_dir = Path(__file__).parent.parent.parent.parent
    config = read_config_from_file(base_dir/"config.yaml")
    shared = Shared(base_dir=base_dir, mode=args.mode, config=config)
    return shared
    

shared:Shared = init_shared_res(args)
