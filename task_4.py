#4. Написать программу, которая генерирует в указанных пользователем границах:
#    случайное целое число;
#    случайное вещественное число;
#    случайный символ.
import random
x1=int(input('Введи целое число x1 = '))
x2=int(input('Введи целое число x2 = '))
x3=random.randint(x1,x2)
print('Cлучайное целое число между ',x1,' и ',x2,' - ',x3)

f1=float(input('Введи вещественное число f1 = '))
f2=float(input('Введи вещественное число f2 = '))
f3=random.randint(x1*1000,x2*1000)/1000 # или random.uniform(A, B)
print('Cлучайное вещественное число между ',f1,' и ',f2,' - ',f3)

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
l1=str(input('Введи символ l1 = '))
l2=str(input('Введи символ l2 = '))
for i in range(0, 26):
    if l1==ALPHABET[i]:
        l1pos=i
    if l2==ALPHABET[i]:
        l2pos=i
l3=ALPHABET[random.randint(l1pos,l2pos)]
print('Cлучайный символ между ',l1,' и ',l2,' - ',l3)
