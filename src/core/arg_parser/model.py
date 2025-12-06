from pydantic import BaseModel
from typing import Optional, List, Any
from enum import Enum

class Mode(Enum):
    GATHER_DATA="gtr-data"
    CLEAN_DATA="clean-data"
    AUGMENT_DATA="aug-data"
    TRAIN="train"
    TEST="test"
    TEXT_ANALYSIS = "text-anl"
    VISUALIZE = "visualize"
    DEBUG = "debug"


class Override(BaseModel):
    keyword:str
    value:Any


class Args(BaseModel):
    mode: Mode
    overrides: List[Override]