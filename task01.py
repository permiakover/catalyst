# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.


# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#  Количество элементов (n) задаётся.

import cProfile

# Вариант 1 - Цикл While


def progress1(n):
    sum_ = 1
    div = -2
    k = 1
    i = 1
    while k < n:
        i /= div
        sum_ += i
        k += 1
    return sum_

#cProfile.run('progress1(10000000)')
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    3.237    3.237 <string>:1(<module>)
#        1    3.237    3.237    3.237    3.237 task01.py:11(progress1)
#        1    0.000    0.000    3.237    3.237 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 31.2 usec per loop - 111
# 100 loops, best of 5: 91.2 usec per loop - 333
# 100 loops, best of 5: 195 usec per loop  - 666
# 100 loops, best of 5: 298 usec per loop  - 999

# Вариант 2 - Цикл for


def progress2(n):
    sum_ = 0
    p = 1
    for i in range(n):
        sum_ += p
        p *= -0.5
    return sum_



#cProfile.run('progress2(10000000)')
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.747    1.747 <string>:1(<module>)
#        1    1.747    1.747    1.747    1.747 task01.py:36(progress2)
#        1    0.000    0.000    1.747    1.747 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 16.7 usec per loop - 111
# 100 loops, best of 5: 50.7 usec per loop - 333
# 100 loops, best of 5: 109 usec per loop  - 666
# 100 loops, best of 5: 171 usec per loop  - 999


# Вариант 3 - Рекурсия - пропущен из-за recursionlimit

def progress3(n):
    b0 = 1
    q = -0.5
    if n == 1:
        return b0
    else:
        return b0 + (n - 1) * q + progress3(n - 1)

#сProfile пропущен из-за recursionlimit

# 100 loops, best of 5:  62  usec per loop - 111
# 100 loops, best of 5:  205 usec per loop - 333
# 100 loops, best of 5:  416 usec per loop  - 666
# 100 loops, best of 5:  618 usec per loop  - 991

# Вариант 4 - Формула


def progress4(n):
    b0 = 1
    st = -0.5
    sum_ = b0 * (1--st**n)/(1 - st)
    return sum_

#cProfile.run('progress4(10000000)')

#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 task01.py:57(progress4)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 813 nsec per loop - 111
# 100 loops, best of 5: 862 nsec per loop - 333
# 100 loops, best of 5: 870 nsec per loop - 666
# 100 loops, best of 5: 887 nsec per loop - 999


# Выводы:
# Иметь аналитическую формулу однозначно выгодно, но не беря ее в расчёт наилучшим выбором
# является реализация 2 на основе цикла for, которая чуть чуть выигрывает у while и имеет туже динамику времязатратности.