def scrabble_game():
    # Ценность буквы: набор букв
    scrabble_dict = {
        1: 'AEILNORSTU',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'
    }

    input_word = input()
    points_sum = 0  # Переменная для суммы очков

    # Внешний цикл перебирает каждый символ в слове. Внутренний цикл проверяет: если символ в данной переменной,
    # к общему сумматору прибавляется связанный ключ
    for symbol in input_word:
        for key, value in scrabble_dict.items():
            if symbol in value:
                points_sum += key
                break
    print(points_sum)


scrabble_game()
