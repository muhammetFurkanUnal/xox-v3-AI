def visualize_row(row):
    poss = [f"pos{i}" for i in range(1, 10)]
    visualize_board(row[poss].tolist())

def visualize_board(board):
    symbols = {1: 'X', -1: 'O', 0: '-'}
    mapped = [symbols[x] for x in board]
    
    for i in range(0, 9, 3):
        print(" ".join(mapped[i:i+3]))