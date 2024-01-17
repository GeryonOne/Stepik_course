"""
На вход программе подается натуральное число n. Напишите программу, которая выводит в порядке возрастания
 все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит n.
"""""

import math
from fractions import Fraction


# Определение функции young_math_lover, которая принимает на вход натуральное число n
def young_math_lover(num):
    # Вызов функции calculate_fractions и получение списка дробей
    fractions_list = calculate_fractions(num)
    # Сортировка списка дробей
    sorted_fractions_list = sorted(fractions_list)
    # Вывод отсортированных дробей, разделенных новой строкой
    print(*sorted_fractions_list, sep='\n')


# Определение функции calculate_fractions, которая возвращает список несократимых дробей
# с суммой числителя и знаменателя num
def calculate_fractions(num):
    # Инициализация списка для хранения дробей
    fraction_list = []

    # Поиск несократимых дробей с заданной суммой числителя и знаменателя
    for denominator in range(1, num+1):
        for numerator in range(1, denominator):
            # Проверка условий: числитель + знаменатель равны num, дробь несократима, числитель меньше знаменателя
            if math.gcd(numerator, denominator) == 1 and numerator < denominator:
                # Добавление дроби в список
                fraction_list.append(Fraction(numerator, denominator))

    return fraction_list


# Ввод натурального числа с клавиатуры
n = int(input())

# Вызов функции young_math_lover с введенным числом в качестве аргумента
young_math_lover(n)
