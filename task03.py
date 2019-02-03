# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random, statistics


def mediansearch(array):
    n = len(array)
    medi = False
    dif = []
    for i in range(0, n):
        bigger = 0
        less = 0
        for j in range(0, n):
            if array[j] != array[i]:
                if array[j] > array[i]:
                    bigger += 1
                else:
                    less += 1
        dif.append(abs(bigger-less))            # если есть несколько одинаковых элементов, то плечи списка относительно
                                                # медианы будут неравнозначными, запоминаем разницу плеч
        if bigger == less:
            medi = array[i]
    if medi:
        return medi
    else:
        return array[dif.index(min(dif))]       # находим медиану по минимальной разнице в плечах


m = 10
size = 2*m+1
array = [random.randint(-101, 100) for _ in range(size)]
# array = [10, 10, 10, 10, 3, 2]                     # тестовый массив с повторяющимися значениями
print(f'Исходный массив\n{array}')
mediana = mediansearch(array)
medianaprove = statistics.median(array)

print(f'Медиана массива = {mediana}')
if mediana == medianaprove:
    print(f'[Проверка результата модулем statistics проведена успешно]')             # проверка другим модулем
else:
    print(f'Что-то посчиталось не так')
