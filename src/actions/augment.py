import pandas as pd
from pathlib import Path
import os
import csv
from pydantic import BaseModel
from ..data_structures import CleanDatasetRow


def import_clean_dataset(path) -> pd.DataFrame:
    return pd.read_csv(path)



def original(row) -> CleanDatasetRow:
    indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def rotate_90_cw(row) -> CleanDatasetRow:
    indices = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def rotate_180(row) -> CleanDatasetRow:
    indices = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def rotate_90_ccw(row) -> CleanDatasetRow:
    indices = [2, 5, 8, 1, 4, 7, 0, 3, 6]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def symmetry_y(row) -> CleanDatasetRow:
    indices = [2, 1, 0, 5, 4, 3, 8, 7, 6]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def rotate_90_cw_symmetry_y(row) -> CleanDatasetRow:
    indices = [0, 3, 6, 1, 4, 7, 2, 5, 8]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def symmetry_x(row) -> CleanDatasetRow:
    indices = [6, 7, 8, 3, 4, 5, 0, 1, 2]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def rotate_90_cw_symmetry_x(row) -> CleanDatasetRow:
    indices = [8, 5, 2, 7, 4, 1, 6, 3, 0]
    target = row[-1] - 1
    new_board = tuple(row[i] for i in indices)
    new_target = indices.index(target)
    return CleanDatasetRow.from_tuple(new_board + (new_target + 1,))



def append_aug_dataset(row: CleanDatasetRow, path: str):
	directory = Path(path).parent
	os.makedirs(directory, exist_ok=True)
	file_exists = os.path.isfile(path)

	data = row.model_dump()

	with open(path, mode='a', newline='', encoding='utf-8') as f:
		writer = csv.DictWriter(f, fieldnames=data.keys())

		if not file_exists:
			writer.writeheader()

		writer.writerow(data)



augmentations = {
    'original': original,
    'rotate_90_cw': rotate_90_cw,
    'rotate_90_ccw': rotate_90_ccw,
    'rotate_180': rotate_180,
    'symmetry_x': symmetry_x,
    'symmetry_y': symmetry_y,
    'rotate_90_cw_symmetry_y': rotate_90_cw_symmetry_y,
    'rotate_90_cw_symmetry_x': rotate_90_cw_symmetry_x
}