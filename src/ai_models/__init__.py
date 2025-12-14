# uncomment if using in agentic mode

# from .MLP import (
# 	MLP as AIModel, 
# 	configure_optimizers,
# 	build_datasets, 
# 	loss_function, 
# 	Humanishset as Dataset
# )

from .ai_model_provider import (
	AIModel,
	AIModelProvider
)