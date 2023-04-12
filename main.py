#Задача 16:


import random

list_1 = []
n_1 = int(input('Введите количество элементов: '))
for i in range(n_1):
        list_1.append(random.randint(-20,20))
print(list_1)
x_1 = int(input('Введите элемент для проверки: '))
print('Количество вхождений: ',list_1.count(n_1))

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
print(f'Элемент под номером {range_indx+1} с значением', list_2[range_indx],'На растоянии ', range_el)


#*Задача 20

dict_1 = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'F':4,
          'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10,
          'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2,
          'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8,
          'Ф':10, 'Щ':10, 'Ъ':10}
x_3 = input('Введите слово для анализа: ')
x_3 = x_3.upper()
sum = 0
for i in range(len(x_3)):
    if dict_1.get(x_3[i]):
        sum += int(dict_1.get(x_3[i]))

print('Количество очков = ', sum)