from pydantic import BaseModel
from typing import List
from ..core import TrainConfig


class TrainResults(BaseModel):

	avg_loss: float
	date: str
	time: str
	train_config: TrainConfig

	# keep this at the end for better readibility
	avg_loss_history: List[float]
	model_config = {
        "arbitrary_types_allowed": True
    }


