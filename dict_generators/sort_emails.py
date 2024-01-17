# Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену.
# Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке,
# в формате username@domain


def main():
    # Домен: юзернейм
    emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
              'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
              'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
              'yandex.ru': ['surface', 'google'],
              'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
              'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

    result_list = print_emails(emails)  # Присвоить переменной result_list отсортированный список почт юзеров
    print(*result_list, sep='\n')  # Вывести данные


def print_emails(emails):
    email_list = []  # Список для добавления почт пользователей
    for domain in emails:  # Внешний цикл перебирает домены
        for username in emails[domain]:  # Во вложенном цикле перебирается каждый юзернейм для домена
            email_list.append(username + '@' + domain)  # Добавить в список каждый адрес электронной почты

    return sorted(email_list)  # вернуть отсортированный список


main()
