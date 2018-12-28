# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# 4. Определить, какое число в массиве встречается чаще всего.

import random

size = 15
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

min_1 = 0
min_2 = 0

for i in range(size):
    if array[i] < array[min_1]:
        min_1 = i

array2 = [k for k in array if k != array[min_1] ]

for i in range(size-1):
    if array2[i] < array2[min_2]:
        min_2 = i

if min_1 <= min_2:
    min_2 += 1

print('Исходный массив:')
print(array)

print('Первое минимальное число: ', array[min_1], ' в позиции: ', min_1+1)
print('Второе минимальное число: ', array[min_2], ' в позиции: ', min_2+1)
