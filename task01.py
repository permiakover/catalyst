# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = []
krat = [0]*8

for i in range(2, 100):
    array.append(i)
    for j in range(2, 10):
        if i % j == 0:
            krat[j-2] += 1

print('Массив натуральных чисел от 2 до 99:')
print(array)

k = 0
while k < len(krat):
    print('Количество чисел кратных ', k+2, ' = ', krat[k])
    k += 1


