from mydescription import show_size_globals
size1 = 5
size2 = 3
print('Введи последовательно элементы матрицы', size1-1, 'х', size2, ': ')
matrix1 = [[int(input('Следующий элемент ... ')) for _ in range(size2)] for _ in range(size1)]
print('\nВведенная матрица:')
for line in matrix1:
    print(line)
matrix2 = [[0 for _ in range(size2+1)] for _ in range(size1)]

for i in range(size1):
    sum_ = 0
    for j in range(size2):
        matrix2[i][j] = matrix1[i][j]
        sum_ += matrix1[i][j]
    matrix2[i][j+1] = sum_

print('Полученная матрица:')
for line in matrix2:
    print(line)

G = globals()
#print(G)
print(show_size_globals(G))



