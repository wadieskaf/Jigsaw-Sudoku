import numpy as np

with open('sudoku_Regions.txt') as f:
    content = f.read()
dict_construct = 'regions_dict = {' + content + '}'
regions_dict = {}
exec(dict_construct)
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def construct_sudoku_array():
    with open('sudoku.txt') as f:
        file_content = list(filter((lambda x: x != ',' and x != '\n'), list(f.read())))
    sudoku_array = np.array(file_content, dtype=int).reshape(9, 9)
    return sudoku_array


def find_empty(x):
    for index, item in np.ndenumerate(x):
        if item == 0:
            return (index)
    return None


def find_region(i, j):
    for v, d in regions_dict.items():
        if (i, j) in d:
            return v


def find_regional_numbers_set(x, i, j):
    regional_points = regions_dict[find_region(i, j)]
    regional_points_set = set(x[a] for a in regional_points)
    return regional_points_set


def find_available_numbers(x, i, j):
    set_1 = set(x[i, :])
    set_2 = set(x[:, j])
    set_3 = find_regional_numbers_set(x, i, j)
    return numbers_set.difference(set_1.union(set_2.union(set_3)))


def solve(sudoku_array):
    empty_index = find_empty(sudoku_array)
    if not empty_index:
        return True
    available_numbers = find_available_numbers(sudoku_array, empty_index[0], empty_index[1])
    if len(available_numbers) == 0:
        return False
    for x in available_numbers:
        sudoku_array[empty_index] = x
        if solve(sudoku_array):
            return True
        sudoku_array[empty_index] = 0
    return False


sudoku = construct_sudoku_array()
solve(sudoku)
print(sudoku)
