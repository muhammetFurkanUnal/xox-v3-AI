from torch.utils.data import Dataset
import pandas as pd
import torch

class Humanishset(Dataset):
	def __init__(self, csv_path):
		self.df = pd.read_csv(csv_path)
		self.features = self.df.iloc[:, :-1].values
		self.targets = (self.df.iloc[:, -1] - 1).values
		

	def __len__(self):
		return len(self.df)
	

	def __getitem__(self, index):
		features_tensor = torch.tensor(self.features[index], dtype=torch.float32)
		target_tensor = torch.tensor(self.targets[index], dtype=torch.long)
		return features_tensor, target_tensor
	
