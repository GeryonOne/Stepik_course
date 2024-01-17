# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса,
# сформированную из этих параметров

def build_query_string(params_dict):
    params_list = []
    for key, value in params_dict.items():
        params_list.append(key + '=' + str(value))  # Добавить данные словаря в список в формате key=value
    params_list.sort()  # сортировка ключей по возрастанию
    query = '&'.join(params_list)  # Добавить амперсанду & между параметрами в запросе
    return query


print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))