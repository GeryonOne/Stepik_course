import random


def throw_the_dice():

    n = int(input())
    for _ in range(n):
        print(random.randint(1, 6))


throw_the_dice()
