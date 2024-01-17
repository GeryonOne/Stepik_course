"""
Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.
"""""


import random


def create_anagram():
    input_word = input()
    symbol_list = [symbol for symbol in input_word]
    random.shuffle(symbol_list)

    return ''.join(symbol_list)


print(create_anagram())
