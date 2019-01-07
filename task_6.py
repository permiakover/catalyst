# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

POS=int(input('pos = '))

print('Буква с номером ', POS, ' в алфавите это - ', ALPHABET[POS-1])
