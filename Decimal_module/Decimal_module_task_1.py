from decimal import Decimal as d

s = ('9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09'
     ' 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08'
     ' 3.86 5.56 1.43 8.36 6.29 5.13')

decimal_list = [d(i) for i in s.split()]
print(sum(decimal_list))

five_max_nums = []

for i in range(5):
    current_max_num = max(decimal_list)
    five_max_nums.append(current_max_num)
    decimal_list.remove(current_max_num)

for i in five_max_nums:
    print(i, end=' ')
