# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
# постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался

def fix_duplicates():
    input_string = input().split()  # Разбить строку на список из слов. Делается это затем, что в вводимых данных идут
    # не только символы, но и слова
    symbol_count = {}  # Пустой словать. Ключ: слово, значение: количество повторений
    refactored_string_list = []  # Список, в который добавляются слова после проверки

    for current_word in input_string:  # Пройтись во списку
        if current_word == ' ':  # Пропустить пробелы
            continue

        symbol_count[current_word] = symbol_count.get(current_word, 0) + 1  # Заполнить словарь, подсчитать значения

        if symbol_count[current_word] == 1:  # Если ключ в цикле встретился в первый раз - вывести
            refactored_string_list.append(current_word)
        else:  # Если ключ ранее встречался, добавить идентификатор
            refactored_string_list.append(current_word + '_' + str(symbol_count[current_word] - 1))

    refactored_string = ' '.join(refactored_string_list)  # Преобразовать список в строку, разделить пробелами
    print(refactored_string)


fix_duplicates()
