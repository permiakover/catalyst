# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 15
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

min_ = 0
max_ = 0

for i in range(size):
    if array[i] < array[min_]:
        min_ = i
    elif array[i] > array[max_]:
        max_ = i
print('Исходный массив:')
print(array)
print('\nМассив, в котором минимальное и максимальное значение поменяны местами (нумерация с 1):')
print('Замена позиций ', min_+1, ' и ', max_+1)
tmp = array[min_]
array[min_] = array[max_]
array[max_] = tmp
print(array)