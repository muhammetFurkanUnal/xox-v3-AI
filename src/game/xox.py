from pydantic import BaseModel
from typing import List
from enum import Enum
from .exceptions import *
import secrets

class Player(Enum):
	x = "X"
	o = "O"
	none = "-"


class GameState(BaseModel):
	board:List[Player]
	turn_who: Player
	turn_num: int
	winner: Player
	draw: bool
	game_id: str

	model_config = {
		"arbitrary_types_allowed":True
	}


class XOXGame:

	def __init__(self):
		self.turn_who : Player = Player.x
		self.turn_num : int = 0
		self.board : List[Player] = [Player.none for i in range(9)]
		self.winner : Player = Player.none
		self.draw : bool = False
		self.game_id = secrets.token_hex(3)


	def do_move(self, position):
		if not (0 <= position <= 8):
			raise InvalidPositionError("Position out of boundary!")

		if self.winner != Player.none:
			raise GameOverError("Game is finished already!")

		if self.board[position] != Player.none:
			raise PositionOccupiedError("Position is not empty!")
		
		self.board[position] = self.turn_who
			
		self.turn_num += 1
		self.check_winner()

		if not self.is_finished():
			if self.turn_who == Player.x:
				self.turn_who = Player.o
			else:
				self.turn_who = Player.x



	def reset(self):
		self.turn_who = Player.x
		self.turn_num = 0
		self.board = [Player.none for i in range(9)]
		self.winner = Player.none
		self.draw = False


	def check_winner(self):
		winning_combinations = [
			(0, 1, 2), (3, 4, 5), (6, 7, 8), 
			(0, 3, 6), (1, 4, 7), (2, 5, 8), 
			(0, 4, 8), (2, 4, 6)             
		]

		for a, b, c in winning_combinations:
			if self.board[a] == self.board[b] == self.board[c] and self.board[a] != Player.none:
				self.winner = self.board[a]
				return

		if self.winner == Player.none and self.turn_num == 9:
			self.draw = True

	
	def get_state(self) -> GameState:
		return GameState(
            board=self.board,
            turn_who=self.turn_who,
            turn_num=self.turn_num,
            winner=self.winner,
			draw=self.draw,
			game_id=self.game_id
        )
	

	def is_finished(self):
		return self.winner != Player.none or self.draw == True


	def __str__(self):
		padding_x = 1
		
		rows = [
			" ".join(p.value for p in self.board[i : i+3]) 
			for i in range(0, 9, 3)
		]
		
		raw_width = len(rows[0]) 
		total_width = raw_width + (padding_x * 2)
		
		col_headers = " ".join(str(i) for i in range(1, 4))
		
		gutter_size = 3 
		gutter_space = " " * gutter_size 
		
		header_str = f"{' ' * (gutter_size + padding_x)}{col_headers}"
		
		padded_rows = []
		for idx, row in enumerate(rows):
			row_num = idx + 1
			
			pad_str = " " * padding_x
			line = f"{row_num:<{gutter_size}}{pad_str}{row}{pad_str}"
			padded_rows.append(line)
			
		return f"{header_str}\n" + "\n".join(padded_rows)





if __name__ == "__main__":
	game = XOXGame()
	moves = [0, 1, 3, 6, 4, 5, 8]
	i = 0
	while(not game.is_finished()):
		game.do_move(moves[i])
		i += 1

	print(game)
	print(game.get_state())


