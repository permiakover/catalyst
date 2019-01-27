from mydescription import show_size_globals
N = 5
M = 4
matrix = []
for i in range(N):
    row = []
    summ = 0
    for j in range(M - 1):
        num = int(input(f'{i}-я строка, {j}-й элемент : '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    print(line)

G = globals()
print(G)
print(show_size_globals(G))