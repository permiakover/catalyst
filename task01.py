# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.


from collections import namedtuple

companies = []
company = namedtuple('company', 'title p1 p2 p3 p4 psum')
meantotal=0

k = int(input('Введи количество компаний - '))

print('*'*30, '\n')
print('Осуществляйте ввод данных компании последовательно через пробел - название, прибыль за 1,2,3,4 квартал', '\n')

for i in range(0, k):
    data = str(input(f'Введи данные компании {i+1} и прибыли поквартально\n'))
    c = data.split(' ')

    s = sum([int(c[1]), int(c[2]), int(c[3]), int(c[4])])         # суммарная прибыль за 4 квартала

    newcom = company(c[0], int(c[1]), int(c[2]), int(c[3]), int(c[4]), s)
    companies.append(newcom)
    meantotal += newcom.psum
#print(companies)
meantotal /= k                                                      # средняя прибыль за год

print('*'*30, '\n')
print(f'Средняя прибыль за год = {meantotal}')
print('\nКомпании, чья прибыль за год НИЖЕ средней:', '\n')
for i in range(0, k):
    if companies[i].psum > meantotal:
        print(companies[i].title)
print('\nКомпании, чья прибыль за год НИЖЕ средней:', '\n')
for i in range(0, k):
    if companies[i].psum < meantotal:
        print(companies[i].title)

