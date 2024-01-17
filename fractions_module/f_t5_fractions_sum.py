"""
На вход программе подается натуральное число n. Напишите программу, которая вычисляет и выводит рациональное число,
равное значению выражения: 1/1**2 + 1/2**2 + 1/n**2

"""""
from fractions import Fraction


def find_fractions_sum(num):
    nums_sum = Fraction(0)
    for i in range(1, num + 1):
        nums_sum += Fraction(1, (i**2))

    # limited_sum = Fraction.limit_denominator(nums_sum)
    return nums_sum


n = int(input())
print(find_fractions_sum(n))
