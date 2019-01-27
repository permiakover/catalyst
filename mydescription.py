# Следую вашей рекомендации и исследую программу из 3го урока (task01)
# В сравнение с ней беру программу из урока (task02)


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import sys
# Результаты:

def show_size(x, level=0):

    #print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
    return sys.getsizeof(x)                             # Добавил return

def show_size_globals(G):                               # Для вычисления памяти в словаре Globals

    mem = 0
    cantcalmem = ('__loader__', '__builtins__', 'sys', 'show_size', 'show_size_globals', '__annotations__', 'G')
    for i in G.keys():
        if i not in cantcalmem:
            mem += show_size(G.get(i))
    return mem

#A = [1, 1, 1, 3]
#print(show_size(A))


# Результаты сравнения на Windows 8.1 64 - заполнение только '1'

# task01 = 401
# содержание globals
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00D8CE90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/PLASERO/Desktop/PYTHON/GB.Lesson06/task01.py', '__cached__': None, 'show_size_globals': <function show_size_globals at 0x00DC9DB0>, 'size1': 5, 'size2': 3, 'matrix1': [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 'line': [1, 1, 1, 3], 'matrix2': [[1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3]], 'i': 4, 'sum_': 3, 'j': 2, 'G': {...}}

# task02 = 399
# содержание globals
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02D8CE90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/PLASERO/Desktop/PYTHON/GB.Lesson06/task02.py', '__cached__': None, 'show_size_globals': <function show_size_globals at 0x02EB9DB0>, 'N': 5, 'M': 4, 'matrix': [[1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3], [1, 1, 1, 3]], 'i': 4, 'row': [1, 1, 1, 3], 'summ': 3, 'j': 2, 'num': 1, 'line': [1, 1, 1, 3], 'G': {...}}
#
# Вывод - task02 на 0,5% эффективнее по использованию памяти