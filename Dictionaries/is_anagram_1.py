def is_anagram():
    word_1, word_2 = input(), input()
    word_dict_1 = {}
    word_dict_2 = {}

    for symbol in word_1:
        word_dict_1[symbol] = word_dict_1.get(symbol, 0) + 1

    for symbol in word_2:
        word_dict_2[symbol] = word_dict_2.get(symbol, 0) + 1

    if word_dict_1 == word_dict_2:
        print('YES')
    else:
        print('NO')


is_anagram()
