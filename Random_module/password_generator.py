"""
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных и 
прописных английских букв и цифр, кроме тех, которые легко перепутать между собой: 'lI1Oo0'

Формат входных данных
На вход программе подаются два числа n и m, каждое на отдельной строке.

Формат выходных данных:
Программа должна вывести  n паролей длиной m символов в соответствии с условием задачи, каждый на отдельной строке.

Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной 
букве в верхнем и нижнем регистре.

"""""
import random
import string as st


def pass_generator():
    # Генерация строки, состоящей из строчных и прописных букв английского алфавита и цифр,
    # исключая символы 'lI1oO0', которые могут быть легко перепутаны
    letters = ''.join((set(st.ascii_letters).union(set(st.digits))) - set('lI1oO0'))

    # Ввод пользователем количества паролей и их длины
    count_of_passwords, pass_length = (int(input("Введите необходимое количество паролей (не менее 1-го): ")),
                                       int(input("Введите необходимую длину пароля (не менее 3-х символов: ")))

    # Генерация паролей и вывод на экран
    generated_passwords_list = generate_passwords(count_of_passwords, pass_length, letters)
    print(*generated_passwords_list, sep='\n')


def generate_passwords(count, length, letters):
    # Генерация списка паролей
    password_list = []

    while len(password_list) < count:
        # Каждый пароль генерируется с помощью отдельной функции generate_password(length, letters)
        created_pass = generate_password(length, letters)

        if pass_validation(created_pass):
            password_list.append(created_pass)

    # Вернуть сгенерированный список паролей
    return password_list


def generate_password(length, letters):
    # Генерация одного пароля заданной длины
    generated_pass = ''

    for symbol in range(length):
        # Каждый символ в пароле генерируется с помощью случайного выбора элемента из строки letters
        generated_pass += random.choice(letters)

    return generated_pass


def pass_validation(password):
    # Проверка наличия цифры, буквы в верхнем и нижнем регистре в пароле
    return (any(char.isdigit() for char in password) and any(char.isupper() for char in password)
            and any(char.islower() for char in password))


# Вызов функции для генерации и вывода паролей
pass_generator()
