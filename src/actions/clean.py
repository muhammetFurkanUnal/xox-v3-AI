import pandas as pd
import numpy as np
from typing import List
from pathlib import Path

def import_raw_dataset(path) -> pd.DataFrame:
    dtype_map = {
    'pos1': 'int8', 'pos2': 'int8', 'pos3': 'int8',
    'pos4': 'int8', 'pos5': 'int8', 'pos6': 'int8',
    'pos7': 'int8', 'pos8': 'int8', 'pos9': 'int8',
    'winner': 'int8',
    'draw': 'int8',        
    'move_number': 'int8', 
    'next_player': 'int8'
    }
    return pd.read_csv(
        path,
        dtype=dtype_map,
        )


def find_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Find best position to play (target) in the current game state, add as a new column.
    Keeps all game states including finished games.
    For finished games (no next move), target is 0.
    """
    board_cols = [f"pos{i}" for i in range(1, 10)]
    next_board = df.groupby("game_id")[board_cols].shift(-1)
    diff = (next_board - df[board_cols]).abs()
    valid_mask = diff.notna().all(axis=1)
    
    df_clean = df.copy()
    df_clean["target"] = 0
    df_clean.loc[valid_mask, "target"] = np.argmax(diff[valid_mask].values, axis=1) + 1
    
    return df_clean


def XO_draw_split(df: pd.DataFrame) -> pd.DataFrame:

    """
    Splits datasets into 4 parts
    """

    winner_x_ids = df[df["winner"] == 1]["game_id"].unique()
    winner_o_ids = df[df["winner"] == -1]["game_id"].unique()
    draw_ids = df[df["draw"] == 1]["game_id"].unique()

    winner_x_moves = df[df["game_id"].isin(winner_x_ids) & (df["next_player"] == 1)]
    
    winner_o_moves = df[df["game_id"].isin(winner_o_ids) & (df["next_player"] == -1)]
    
    draw_x_moves = df[df["game_id"].isin(draw_ids) & (df["next_player"] == 1)]

    draw_o_moves = df[df["game_id"].isin(draw_ids) & (df["next_player"] == -1)]
    
    return winner_x_moves, winner_o_moves, draw_x_moves, draw_o_moves


def drop_extras(df: pd.DataFrame) -> pd.DataFrame:
    cols_to_drop = ["winner", "draw", "move_number", "next_player", "game_id"]
    df_clean = df.drop(cols_to_drop, axis=1)
    df_clean = df_clean[df_clean["target"] != 0]
    return df_clean


def switch_OX(df: pd.DataFrame) -> pd.DataFrame:
	_df = df*-1
	_df["target"] *= -1
	return _df


def merge_dfs(dfs: List[pd.DataFrame]) -> pd.DataFrame:
     return pd.concat(dfs, ignore_index=True)


def save_clean_dataset(df: pd.DataFrame, path):
    p = Path(path)
    parent = p.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)


