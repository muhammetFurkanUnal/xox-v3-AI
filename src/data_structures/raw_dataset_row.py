from pydantic import BaseModel
from ..game import GameState, Player

class RawDatasetRow(BaseModel):

	pos1: int  # 1:X, -1: O, 0: empty
	pos2: int
	pos3: int
	pos4: int
	pos5: int
	pos6: int
	pos7: int
	pos8: int
	pos9: int
	winner: int  # 1: X, -1: O, 0: no one 
	draw: int  # 0: not draw, 1: draw
	move_number: int
	next_player: int  # 1: X, -1: O
	game_id: str
