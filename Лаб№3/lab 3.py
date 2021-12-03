import csv
import sys
grp=int(input("Выберите группу студентов: 1- Экономика, 2-Маркетинг"))
if grp==1:
    oper=int(input("Выберите действие:1 - Прочитать файл, 2 - Перезаписать файл, 3 - Добавить в файл, 4 - Найти данные в файле, 5 - Отсортировать по среднему баллу "))
    if oper==1:
        file=open('students.txt', 'r', encoding='utf-8')
        print(file.read())
        file.close()
    elif oper==2:
        newstud=(input("Введите ФИО студентов и их балл"))
        file=open('students.txt','w',encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3:
        grade=input("Введите балл ЗНО ")
        addstud=input("ФИО кого добавить ")
        file=open('students.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4:
        file=open ('students.txt', 'r', encoding ='utf-8')
        search=input('ФИО кого найти')
        read=file.read()
        file.close()
        if search in read :
            print("Найден")
        else :
            print("Не найден")
    elif oper == 5 :
        file = open('students.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')
else : 
    oper=int(input("Выберите действие:1 - Прочитать файл, 2 - Перезаписать файл, 3 - Добавить в файл, 4 - Найти данные в файле, 5 - Отсортировать по среднему баллу "))
    if  oper == 1 :
        file = open('students2.txt', encoding ='utf-8')
        print(file.read())
        file.close()
    elif oper == 2 :
        newstud=(input("Введите ФИО студентов и их балл"))
        file = open('students2.txt','w', encoding ='utf-8')
        file.write(newstud)
        file.close()
    elif oper == 3 :
        grade = input("Введите балл ЗНО ")
        addstud = input("ФИО кого добавить ")
        file = open('students2.txt','a', encoding ='utf-8')
        file.write ('\n' +grade+ " " +addstud)
        file.close()
    elif oper == 4 :
        file = open ('students2.txt', 'r', encoding = 'utf-8')
        search = input('ФИО кого найти')
        read= file.read()
        file.close()
        if search in read :
            print("Найден")
        else :
            print("Не найден")
    elif oper == 5 :
        file = open('students2.txt', encoding ='utf-8')
        for i in sorted(file) :
            print(i, end= ' ')