#Задача 16:


import random
"""
list_1 = []
n_1 = int(input('Введите количество элементов: '))
for i in range(n_1):
        list_1.append(random.randint(-20,20))
print(list_1)
x_1 = int(input('Введите элемент для проверки: '))
print('Количество вхождений: ',list_1.count(x))
"""
#Задача 18:
list_2 = []
n_2 = int(input('Введите количество элементов: '))
for i in range(n_2):
        list_2.append(random.randint(-10,20))
print(list_2)
x_2 = int(input('Введите элемент для проверки: '))
range_indx = 0
range_el = x_2 - list_2[range_indx]

for i in range(len(list_2)):
        if (abs(x_2 - list_2[i]) < range_el):
            range_indx = i
            range_el = abs(x_2 - list_2[i])
print(f'Элемент под номером {range_indx+1} со значением', list_2[range_indx],'На растоянии ', range_el)


#*Задача 20

