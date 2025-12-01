from ..game import XOXGame, Player, GameState
from ..game.exceptions import *
from ..core import clear_terminal
import time
from ..data_structures import DatasetRow
import os
import csv
from pathlib import Path

def pos_to_row_col(position):
	row = position // 3
	col = position % 3
	return (row+1, col+1)


def row_col_to_pos(row, col):
	row -= 1
	col -= 1
	return row*3 + col


def recieve_pos(pos_str):
	pos_list = pos_str.split(" ")
	if len(pos_list) == 1:
		position = row_col_to_pos(int(pos_str[0]), int(pos_str[1]))
	else:
		position = row_col_to_pos(int(pos_list[0]), int(pos_list[1]))
	return position


def state_to_csv_row(state: GameState) -> DatasetRow:

	PLAYER_TO_INT = {
    Player.x: 1,
    Player.o: -1,
    Player.none: 0
	}

	board_data = {
		f"pos{i}": PLAYER_TO_INT[p] for i, p in enumerate(state.board, 1)
	}

	return DatasetRow(
		**board_data,
		winner=PLAYER_TO_INT[state.winner],
		draw=int(state.draw),  # True -> 1, False -> 0
		move_number=state.turn_num,
		who_played=PLAYER_TO_INT[state.turn_who],
		game_id=state.game_id
	)


def append_dataset(row: DatasetRow, path: str):
	directory = Path(path).parent
	os.makedirs(directory, exist_ok=True)
	file_exists = os.path.isfile(path)

	data = row.model_dump()

	with open(path, mode='a', newline='', encoding='utf-8') as f:
		writer = csv.DictWriter(f, fieldnames=data.keys())

		if not file_exists:
			writer.writeheader()

		writer.writerow(data)


def gather_loop(dataset_file_path):
	while True:
		game = XOXGame()
		rows = []
		reset_flag = False
		while not game.is_finished():
			clear_terminal()
			print(game)
			_in = input("enter row col (example: 2 3 or 23): ")
			if _in == "r":
				reset_flag = True
				break
			else:
				position = recieve_pos(_in)

			try:
				game.do_move(position)
			except InvalidPositionError as e:
				print("Error: ", e)
				time.sleep(1)
			except PositionOccupiedError as e:
				print("Error: ", e)	
				time.sleep(1)		
			except GameOverError as e:
				print("Error: ", e)	
				time.sleep(1)

			row = state_to_csv_row(game.get_state())
			rows.append(row)

		if reset_flag == False:
			for row in rows:
				append_dataset(row, dataset_file_path)

		clear_terminal()
		print(game)
		print(f"Game over!\nWinner: {game.winner.value}")
		time.sleep(1)

