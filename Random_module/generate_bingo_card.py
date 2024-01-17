"""
Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75
 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).
 Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
"""""


import random


def generate_bingo_card():
    bingo_set = set()
    bingo_matrix = []

    while len(bingo_set) < 25:
        bingo_set.add(random.randint(1, 75))

    bingo_matrix = [[bingo_set.pop() for num in range(5)] for _ in range(5)]
    bingo_matrix[2][2] = 0

    print_matrix(bingo_matrix)


def print_matrix(created_matrix):
    bingo_matrix = created_matrix

    for i in range(5):
        for j in range(5):
            print(str(bingo_matrix[i][j]).ljust(3), end=' ')
        print()


generate_bingo_card()
