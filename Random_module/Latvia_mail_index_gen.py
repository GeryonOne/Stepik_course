import random
import string


"""
Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского 
алфавита, Number – число от 0 до 99 (включительно).
Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный 
почтовый индекс Латверии.
Корректный вариант: AB23_56VG  
"""""


def generate_index():
    upper_letters = string.ascii_uppercase
    correct_index = random.choice(upper_letters) + random.choice(upper_letters) + str(random.randrange(0,100)) + '_' + str(random.randrange(0,100)) + random.choice(upper_letters) + random.choice(upper_letters)

    return correct_index


print(generate_index())
