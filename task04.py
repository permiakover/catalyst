# 4. Определить, какое число в массиве встречается чаще всего.

import random

size = 15
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

moda = array[0]
frmax = 1
for i in range(size):
    fr = 1
    for j in range(i + 1, size):
        if array[i] == array[j]:
            fr += 1
    if fr > frmax:
        frmax = fr
        moda = array[i]

print('Исходный массив:')
print(array)

if frmax != 1:
    print('\nЧисло ', moda, ' встречается в исходном массиве', frmax, 'раз')
else:
    print('\nВ исходном массиве нет повторяющихся цифр')