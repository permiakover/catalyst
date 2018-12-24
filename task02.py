# 2. Посчитать четные и нечетные цифры введенного натурального числа.
a = int(input('Введи натуральное число - '))
even = 0
odd = 0
atmp = a
chis = 0

while atmp > 0:
    chis = atmp % 10
    atmp = atmp // 10

    if chis % 2 == 0:
        even += 1
    else:
        odd += 1
print('В введенном натуральном числе ', a,': четных цифр - ', even,' , нечётных - ', odd)