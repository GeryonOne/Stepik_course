import random


def matrix_shuffle():
    matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

    for inner_list in matrix:
        random.shuffle(inner_list)

    return matrix


matrix = matrix_shuffle()
