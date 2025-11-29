from pydantic import BaseModel
from typing import List, Any

class TestResults(BaseModel):
    
    avg_loss: float
    loss_each_epoch = List[float]
    f1_loss: float
    accuracy: float
    precision: float
    recall: float
    roc_auc: float
    pr_auc: float
    
    
    model_config = {
        "arbitrary_types_allowed": True
    }