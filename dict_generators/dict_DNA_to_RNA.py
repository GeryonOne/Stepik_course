# На вход - цепь ДНК. Нужно вывести ее перевод в цепь РНК

def gen_transfer():
    dna_transfer = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}  # Символ в ДНК: Символ в РНК
    dna_chain = input().upper()  # Ввод ДНК
    for symbol in dna_chain:  # Для каждого символа в цепи ДНК вывести интерпретацию в РНК
        print(dna_transfer[symbol], end='')


gen_transfer()
