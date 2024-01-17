import random


def heads_and_tails():
    game_dict = {
        0: 'Орел',
        1: 'Решка'
    }

    for _ in range(int(input())):
        print(game_dict[random.randint(0, 1)])


heads_and_tails()
