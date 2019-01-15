# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

#import cProfile


def searchsimple1(n):

    simplenum = 2
    k = 0
    i = 2
    while k < n:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0

        if flag:
            k += 1
            simplenum = i
        i += 1
    return simplenum

# cProfile.run('searchsimple1(500)')

#      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.782    0.782 <string>:1(<module>)
#         1    0.782    0.782    0.782    0.782 task02.py:5(searchsimple1)
#         1    0.000    0.000    0.782    0.782 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 790 msec per loop  - 500
# 100 loops, best of 5: 137 msec per loop  - 250
# 100 loops, best of 5: 23 msec per loop   - 125
# 100 loops, best of 5: 3.91 msec per loop - 64



def searchsimple2(n):
    k = 0
    loop = 1
    N = 500

    while k < loop:
        # Создание решета
        NN = N * (k + 1)
        a = [0] * NN
        for i in range(0, NN):
            a[i] = i
        a[1] = 0
        m = 2  #

        # Просеивание решета
        while m < NN:
            if a[m] != 0:
                j = m * 2
                while j < NN:
                    a[j] = 0
                    j = j + m
            m += 1

        k += 1
        loop += 1
        # Выделение простого числа
        t = 0
        for i in a:
            if a[i] != 0:
                t += 1
                if t == n:
                    simplenum = a[i]
                    loop -= 1

    return simplenum

#cProfile.run('searchsimple2(500)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#        1    0.019    0.019    0.019    0.019 task02.py:29(searchsimple2)
#        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100 loops, best of 5: 17 msec per loop   - 500
# 100 loops, best of 5: 4.61 msec per loop - 250
# 100 loops, best of 5: 1.34 msec per loop - 125
# 100 loops, best of 5: 428 usec per loop  - 64



# Вывод:
# Оба алгоритма выполнены без break - для "равных" условий
# Алгоритм на основе решета (2) работает в разы быстрее (1), и время затраты его растут меньшими темпами
# Решето решает лучше



