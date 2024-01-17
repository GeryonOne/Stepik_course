import random
import string


def pass_generation(pass_length):
    password = ''
    for _ in range(pass_length):
        password += random.choice(string.ascii_letters)
    return password


def data_input():
    n = int(input())
    generated_pass = pass_generation(n)
    print(generated_pass)


data_input()
