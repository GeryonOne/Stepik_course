"""
Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем.
Вчера на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя,
и несократимой, если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с правильными
несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число n. Напишите программу, которая находит наибольшую правильную несократимую
дробь с суммой числителя и знаменателя равной n.
"""""

# Импорт необходимых модулей
import math
from fractions import Fraction


# Определение функции young_math_lover, которая принимает на вход натуральное число n
def young_math_lover(num):
    # Вызов функции calculate_fractions и получение списка дробей
    fractions_list = calculate_fractions(num)

    # Вывод максимальной дроби из списка
    print(max(fractions_list))


# Определение функции get_nums (не используется в данной задаче)
def get_nums(number):
    nums_list = []
    # Заполнение списка числами от 1 до number-1
    for i in range(1, number):
        nums_list.append(i)

    return nums_list


# Определение функции calculate_fractions, которая возвращает список несократимых дробей
# с суммой числителя и знаменателя num
def calculate_fractions(num):
    # Инициализация списка для хранения дробей
    fraction_list = []

    # Вычисление числителя и знаменателя в зависимости от четности/нечетности num
    for numerator in range((num - 1) // 2, 0, -1):
        denominator = num - numerator

    # Поиск несократимых дробей с заданной суммой числителя и знаменателя
        while numerator > 0 and denominator < num:
            # Проверка условий: числитель + знаменатель равны num, дробь несократима, числитель меньше знаменателя
            if numerator + denominator == num and math.gcd(numerator, denominator) == 1 and numerator < denominator:
                # Добавление дроби в список
                fraction_list.append(Fraction(numerator, denominator))
            # Уменьшение числителя и увеличение знаменателя
            numerator -= 1
            denominator += 1

    return fraction_list


# Ввод натурального числа с клавиатуры
n = int(input())

# Вызов функции young_math_lover с введенным числом в качестве аргумента
young_math_lover(n)
