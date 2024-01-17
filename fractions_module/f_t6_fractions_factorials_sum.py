"""
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число,
 равное значению выражения 1/1! + 1/2! + 1/3! +1/n!
"""""


from fractions import Fraction


def sum_fractions_factorials(num):
    nums_sum = Fraction(0)
    current_factorial, i_factorial = 1, 1

    for i in range(1, num + 1):
        current_factorial *= i
        nums_sum += Fraction(1, current_factorial)

    return nums_sum


n = int(input())
print(sum_fractions_factorials(n))
