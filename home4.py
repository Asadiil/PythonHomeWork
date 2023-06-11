#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.


from random import randint
n_set = set(randint(1, 50) for i in range(int(input("Введите количество элементов первого множества: "))))
print(n_set)
m_set = set(randint(1, 50) for i in range(int(input("Введите количество элементов второго множества: "))))
print(m_set)
e_set = sorted(n_set.intersection(m_set))
print(*e_set)

#Задача 24
n = 5
from random import randint
list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res, 'ягод')
