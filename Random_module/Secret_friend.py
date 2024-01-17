"""
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.

Формат входных данных
На вход программе в первой строке подается число n – общее количество учеников. Далее идут n строк, содержащих имена и фамилии учеников.
Формат выходных данных
Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком) и имя и фамилию его тайного друга, разделённые дефисом.
"""""

import random


def secret_friend():
    # Создаем список учеников с помощью функции create_student_data()
    students_list = create_student_data()

    # Распределяем тайных друзей для каждого ученика с помощью функции student_distribute (students_list)
    student_pair_dict = student_distribute(students_list)

    # Выводим информацию о тайных друзьях
    print_info(student_pair_dict)


def create_student_data():
    # Функция собирает данные об учениках: количество и имена/фамилии
    students_list = []
    for _ in range(int(input())):
        current_student = input()
        # Добавить введенного студента в список
        students_list.append(current_student)

    return students_list


def student_distribute(students_list):
    # Создаем копию списка учеников
    pair_list = students_list.copy()

    # Инициализируем словарь для хранения пар "ученик - тайный друг".
    # Задаем None значения к ключам для корректной работы генератора while
    student_pair_dict = {key: None for key in pair_list}

    # Пока есть ученики без тайных друзей
    while None in student_pair_dict.values():
        # Проходим по каждому ученику
        for student in students_list:
            # Выбираем случайного тайного друга из оставшихся
            random_pair = random.choice(pair_list)

            # Проверяем, что выбранный тайный друг еще не назначен другому ученику
            if random_pair not in student_pair_dict.values():
                # Проверяем, что ученик не может быть своим собственным тайным другом
                if student != random_pair:
                    student_pair_dict[student] = random_pair

    # Вернуть итоговый словарь. Ученик: другой ученик ему в пару
    return student_pair_dict


def print_info(pair_dict):
    # Выводим информацию о тайных друзьях в формате "ученик - тайный друг"
    for key, value in pair_dict.items():
        print(f'{key} - {pair_dict[key]}')


# Вызываем основную функцию
secret_friend()
