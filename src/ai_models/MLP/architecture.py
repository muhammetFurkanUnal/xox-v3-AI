import pandas as pd
import torch
import torch.nn as nn

class MLP(nn.Module):
	
	def __init__(self, layers):
		super().__init__()
		self.fcs = nn.ModuleList()
		for i in range(len(layers) - 1):
			input_size = layers[i]
			output_size = layers[i+1]
			self.fcs.append(nn.Linear(input_size, output_size))
			if i < len(layers) - 2:
				self.fcs.append(nn.BatchNorm1d(output_size))
				self.fcs.append(nn.ReLU())

		
	def forward(self, x):
		for layer in self.fcs:
			x = layer(x)

		return x
