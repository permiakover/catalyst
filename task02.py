# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

def ChangeHex(de, n):   # Пришлось порыться в инете и найти рекурсивную функцию и доработать её

    if n < 0:
        de.append(str(0))
    elif n <= 1:
        de.append(str(n))
    else:
        ChangeHex(de, n // 16)
        x = (n % 16)
        if x < 10:
            de.append(str(x))
        if x == 10:
            de.append("A")
        if x == 11:
            de.append("B")
        if x == 12:
            de.append("C")
        if x == 13:
            de.append("D")
        if x == 14:
            de.append("E")
        if x == 15:
            de.append("F")
    res = de
    return res

from collections import defaultdict, deque

num1 = deque(input('Введи первое HEX число - ').upper())
num2 = deque(input('Введи второе HEX число - ').upper())

num1.reverse()
num2.reverse()

hexs = list('0123456789ABCDEF')
d = defaultdict(int)
k = 0
for hexs in hexs:
    d[hexs] = k
    k += 1

num1dex = 0
num2dex = 0
                                              # Решил считать в десятичной, а потом снова обратно переводить
for i in range(0, len(num1)):
    num1dex += d[num1[i]] * 16**i
for i in range(0, len(num2)):
    num2dex += d[num2[i]] * 16**i

sumdex = num1dex + num2dex
#print(f'Сумма dex = {sumdex}')
proddex = num1dex * num2dex
#print(f'Произведение dex = {proddex}')

sumhex = deque()
prodhex = deque()

S = ChangeHex(sumhex, sumdex)
P = ChangeHex(prodhex, proddex)
if S[0] == '0':
    S.popleft()
if P[0] == '0':
    P.popleft()
print(f'\nСумма введенных чисел = {list(S)}')
print(f'Произведение введенных чисел = {list(P)}')
