"""
IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random генерирует и возвращает случайный корректный IP адрес
Правильный IP адрес: 192.168.5.250
"""

import random


def generate_ip():
    ip_address = []
    for _ in range(4):
        ip_address.append(random.randint(0, 255))

    ip_str = '.'.join(str(i) for i in ip_address)
    return ip_str


random_ip = generate_ip()
print(random_ip)
