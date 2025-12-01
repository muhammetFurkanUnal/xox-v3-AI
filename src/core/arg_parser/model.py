from pydantic import BaseModel
from typing import Optional, List, Any
from enum import Enum

class Mode(Enum):
    TRAIN="train"
    TEST="test"
    GATHER_DATA="gtr-data"
    TEXT_ANALYSIS = "text-anl"
    VISUALIZE = "visualize"
    DEBUG = "debug"


class Override(BaseModel):
    keyword:str
    value:Any


class Args(BaseModel):
    mode: Mode
    overrides: List[Override]