# Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу
# возвращала значения из этого словаря

# Ввод: В первой строке задано одно целое число n — количество слов в словаре. В следующих n строках записаны слова и их
# определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество
# поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке
# Вывод данных: Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести
# его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек
def main():
    number_of_words = int(input())  # Размер словаря с определениями
    slang_dict = create_dict(number_of_words)  # присвоить переменной результат выполнения функции create_dict
    run_search(slang_dict)  # Вызвать функцию run_search для поиска по созданному словарю. Передать данный словарь


# Создать словарь. В цикле задается значение текущей строке. Строка имеет вид "Змея: язык программирования Python".
# Разделить данную строку на 2 куска с помощью .split(':'). Слева - ключ, справа - значение
def create_dict(num_of_words):
    slang_dict = {}
    for i in range(num_of_words):  # цисло итераций цикла задано вручную, в строке №10
        current_string = input()
        chunks = current_string.split(':')
        key = chunks[0].strip().lower()  # Убрать лишние пробелы, исправить регистр для корректного поиска
        value = chunks[1].strip()
        slang_dict[key] = value  # Добавить пару ключ: значение в словарь

    return slang_dict  # Вернуть заполненный словарь. В словаре лежат определения и их значения


# Поиск по ранее созданному словарю. Ввести количество запросов. В цикле ввести каждый конкретный запрос.
# Этот запрос-ключ. По данному ключу найти значение, вывести в терминал. Если значения нет - вывести "Не найдено"
def run_search(slang_dict):
    search_count = int(input())  # Число поисковых запросов задается вручную
    for i in range(search_count):
        current_keyword = input()
        print(slang_dict.get(current_keyword.lower(), "Не найдено"))


main()
