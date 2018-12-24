# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


print('Вводи натуральные числа, 0 - остановка')
maxnsum = 0
nsum = 0

tmp = 0
n = None

while n != 0:
    n = int(input(' '))
    tmp = n
    nsumt = 0
    while tmp > 0:
        nsumt += tmp % 10
        tmp //= 10

    if nsumt > nsum:
        nsum = nsumt
        maxnsum = n
if nsum > 0:
    print('Наибольшее по сумме цифр число - ', maxnsum, ' (сумма цифр = ', nsum, ')')
else:
    print('Числа не введены')




