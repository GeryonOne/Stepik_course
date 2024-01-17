# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.У каждого из друзей Тимура может
# быть один или более номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга

# Ввод данных
# В первой строке задано одно целое число n — количество номеров телефонов, информацию о которых Тимур сохранил в
# телефонной книге. В следующих n строках заданы телефоны и имена их владельцев через пробел. В следующей строке
# записано целое число m — количество поисковых запросов от Тимура. В следующих m строках записаны сами запросы, по
# одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти

# Вывод данных
# Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем

# 1, Мой вариант
def phone_book():
    book_dict = {}  # Ключ - номер телефона. Значение - имя в записной книжке
    for _ in range(int(input())):
        num_and_name = input().lower().split()  # Вводится номер телефона и строка. Затем нижний регистр, создать список
        phone_num, username = num_and_name[0], num_and_name[1]  # Переменные для удобства
        book_dict[phone_num] = username  # Заполнить словарь. Номер телефона: имя в Контактах

# Цикл для поисковых запросов
    for _ in range(int(input())):
        search_name = input().lower()  # Ввести данные, поставить нижний регистр
        search_count = 0  # Счетчик для обработки негативного сценария
        nums_list = []
        for key, value in book_dict.items():  # Разбить текущую пару словаря по переменным
            if search_name == value:  # Если запрос совпал со значением, добавить ключ(номер) в список
                search_count += 1
                nums_list.append(key)
# Важно: данную проверку нужно выполнить в конце прохождения вложенного цикла
        if search_count == 0:  # Сценарий, если в словаре нет поискового запроса
            print('абонент не найден')
        else:
            print(*nums_list)


phone_book()

# 2, Более короткий вариант с методами get, setdefault()
dct = {}  # Ключ: Имя в Контактах. Значение - список номеров телефона
# Цикл для заполнения словаря
for _ in range(int(input())):
    phone, name = input().lower().split()  # Ввод, регистр, разбить на список, присвоить значения переменным
    # Заполнить словарь: проверить, существует ли в словаре ключ name. Если да, вернуть значение (список), добавить
    # в него новый номер телефона. Если данного ключа нет, создать ключ, добавить значение []. Затем к данному пустому
    # списку добавить новый номер телефона
    dct.setdefault(name, []).append(phone)
# цикл для поиска
for _ in range(int(input())):
    print(*dct.get(input().lower(), ['абонент не найден']))  # Вывести информацию по поисковому запросу: если запрос
# совпадает с ключом (Имя в Контактах), развернуть список, вывести все номера. Если нет - вывести текст
