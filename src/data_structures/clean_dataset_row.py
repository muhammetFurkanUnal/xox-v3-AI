from pydantic import BaseModel

class CleanDatasetRow(BaseModel):

	pos1: int  # 1:X, -1: O, 0: empty
	pos2: int
	pos3: int
	pos4: int
	pos5: int
	pos6: int
	pos7: int
	pos8: int
	pos9: int
	target: int

	@classmethod
	def from_tuple(cls, t):
		fields = ['pos1', 'pos2', 'pos3', 'pos4', 'pos5', 'pos6', 'pos7', 'pos8', 'pos9', 'target']
		return cls(**dict(zip(fields, t)))