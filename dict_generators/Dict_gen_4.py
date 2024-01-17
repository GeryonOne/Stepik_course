numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

# Ключ: число в текущей итерации цикла. Значение: список делителей по возрастанию, начиная с 1.
# В значении формируется внутренний генератор: добавить делитель, если выполняется целочисленное деление числа внешнего
# цикла на него без остатка (if i % j == 0). У цикла обратный порядок, чтобы была сортировка по возрастанию
result = {i: [int(i / j) for j in range(i, 0, -1) if i % j == 0] for i in numbers}

print(result)




