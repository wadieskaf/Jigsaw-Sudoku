import numpy as np

with open('Sudoku.txt') as f:
    content = list(filter((lambda x: x != ',' and x != '\n'), list(f.read())))
sudoko_matrix = np.array(content, dtype=int).reshape(9, 9)

print(sudoko_matrix[(0,1)])
