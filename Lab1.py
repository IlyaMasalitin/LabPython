#Задание 1
import math
from termcolor import colored as cl
print(cl('Лабораторная работа 1, Масалітін Ілля ФІТ 1-8','green'))
print("Вариант 21, задание 1\n")
x=int(input("Vvedite znachenie x>>"))
if x>45:
    z = print(-math.sqrt(x))
elif x<=45:
    z = print(math.sin(2*x))
#Задание 2
print("Вариант 21, задание 2\n")
f1=f2=1
print("n = число ряда")
n=int(input("Введите n>>"))
print(f1, end=' ')
print(f2, end=' ')
for i in range(1,n):
    f1, f2 = f2,f1+f2
    print(f2, end=' ')
#Задание 3
print("\nВариант 21, задание 3\n")
print()
N = []
z=int(input("Размер массива>> "))
print ("Введите елементы масива>>")
for i in range (z):
    N.append(int(input()))
print ("Масив>>")
print (N)
print("Среднее арефметическое элементов массива>>")
print((sum(N)/z))
print("Реверсированный массив>>")
N.reverse()
print(N)