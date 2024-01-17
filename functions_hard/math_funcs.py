import math


# Функция для вычисления квадрата числа
def square(num):
    return num ** 2


# Функция для вычисления куба числа
def cube(num):
    return num ** 3


# Функция для вычисления квадратного корня числа
def square_root(num):
    return math.sqrt(num)


# Функция для вычисления модуля числа
def absolute(num):
    return abs(num)


# Функция для вычисления синуса числа
def num_sin(num):
    return math.sin(num)


# Основная функция, объединяющая различные математические функции в словарь и выполняющая выбранную пользователем операцию
def math_functions():
    # Создаем словарь с функциями и их названиями
    func_dict = {'квадрат': square, 'куб': cube, 'корень': square_root, 'модуль': absolute, 'синус': num_sin}

    # Получаем ввод пользователя: число для вычислений и название функции
    calculate_num, func_name = int(input()), input()

    # Выполняем выбранную функцию и выводим результат
    print(func_dict[func_name](calculate_num))


# Вызываем основную функцию
math_functions()
