import torch.optim as optim
from ...core.shared import shared

def configure_optimizers(model):
	return optim.Adam(model.parameters(), lr=shared.config.train.lr)