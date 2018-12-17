# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
N=len(ALPHABET)

L1=int(input('L1 = '))
L2=int(input('L2 = '))

for i in range(0, N):
    print(i)
    if L1==ALPHABET[i]:
        L1pos=i
    if L2==ALPHABET[i]:
        L2pos=i

print('Позиция ', L1, ' в алфавите - ',L1pos+1)
print('Позиция ', L2, ' в алфавите - ',L2pos+1)
print('Между ними ',abs(L1pos-L2pos)-1,' букв')
