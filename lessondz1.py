#Задача 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

number = int(input('Введите цифру дня недели и мы проверим выходной ли это: '))
if number == 1 or number == 2 or number == 3 or number == 4 or number == 5:
   print ('Нет')
elif number == 6 or number == 7:
   print ('Да')
else:
    print ('Такого не существует')

        # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
        # в которой находится эта точка (или на какой оси она находится).

numberX = int(input('Введите число x '))
numberY = int(input('Введите число y '))           
if numberX > 0 and numberY > 0:
    print('1 четверть')
elif numberX < 0 and numberY > 0:
    print('2 четверть')
elif numberX < 0 and numberY < 0:
    print('3 четверть')
elif numberX > 0 and numberY < 0:
    print('4 четверть')
else:
    numberX == 0 and numberY == 0
    print('Координата не должна быть равна 0, введите еще раз')

    # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_chetvert = int(input('Введите номер четверти: '))
if number_chetvert ==  1:
   print('x (0;infinity), y(0;infinity)')
elif number_chetvert ==  2:
    print('x (infinity;0), y(0;infinity)')
elif number_chetvert ==  3:
    print('x (infinity;0), y(infinity;0)')
elif number_chetvert ==  4:       
    print('x (0;infinity), y(infinity;0)')
else:
    print('Такой четверти нет')
    
    # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
    
numberX1= int(input('Введите X1: '))
numberY1= int(input('Введите Y1: '))
numberX2= int(input('Введите X2: '))
numberY2= int(input('Введите Y2: '))
#print(f"Длина отрезка: {format((numberY1-numberY2) **2 + (numberX1-numberX2)**2)}")
from math import sqrt
print('Длина отрезка: ',round(sqrt((numberX1 - numberX2)**2 + (numberY1 - numberY2)**2), 2))


            