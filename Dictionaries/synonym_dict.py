def synonym_dict():
    dict_length = int(input())
    syn_dict = {}

    for i in range(dict_length):
        words_pair = input().split()
        syn_dict[words_pair[0]] = words_pair[1]
        syn_dict[words_pair[1]] = words_pair[0]

    find_synonym = input()
    searched_word = syn_dict[find_synonym]
    print(searched_word)


synonym_dict()
