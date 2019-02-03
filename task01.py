# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def better_bubble(array):


    n = len(array)
    k = n
    obmen_flag = False
    while k > 0:
        for i in range(0, n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                obmen_flag = True
        if k == n:                                          # Улучшил проверкой на необходимость сортировки
            if obmen_flag == False:
                print('Массив не нуждается в сортировке')
                return None
                break
        k -= 1
    res = array
    return res

size = 20
array = [random.randint(-101, 100) for _ in range(size)]
#array = [1, 2, 3, 4, 5]
print(f'Исходный массив\n{array}')
print(f'Отсортированный массив\n{better_bubble(array)}')

