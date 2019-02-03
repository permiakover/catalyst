# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def collide_sort(array):

    n = len(array)
    if n < 2:
        return array
    else:
        m = n // 2
        a1 = collide_sort(array[:m])
        a2 = collide_sort(array[m:])
        return collide(a1, a2)


def collide(a1, a2):
        res = []
      #  print(f'n1 {n1}  n2 {n2}')
      #  print(f'a1 {a1}  a2 {a2}')
        while len(a1)*len(a2):
            if a1[0] < a2[0]:
                res.append(a1[0])
                a1.remove(a1[0])
            else:
                res.append(a2[0])
                a2.remove(a2[0])
        if len(a1) == 0:
            res += a2
        else:
            res += a1
        return res


size = 20
array = [random.uniform(0, 50) for _ in range(size)]
#a1 = [3, 6, 7, 4, 5]
#a2 = [7, 5, 8, 9]
print(f'\nИсходный массив\n')
for i in range(0, size):
    print("%.2f" % array[i], end=' ')

array_sort = collide_sort(array)
print(f'\n\nОтсортированный массив\n')
for i in range(0, size):
    print("%.2f" % array_sort[i], end=' ')
