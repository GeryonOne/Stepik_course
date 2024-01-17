"""
Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно).
Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.
"""
import random


def lottery_ticket():
    win_nums = set()

    while len(win_nums) < 7:
        generated_num = random.randint(1, 49)
        win_nums.add(generated_num)
    sorted_win_nums_set = sorted(win_nums)

    win_nums_string = " ".join([str(i) for i in sorted_win_nums_set])
    print(win_nums_string)


lottery_ticket()
