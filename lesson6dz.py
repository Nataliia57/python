#1 - Определить, присутствует ли в заданном списке строк, некоторое число
lst_len = int(input("Введите количество строк для создания списка: "))
lst = [input(f"Введие {i+1} строку: ") for i in range(lst_len)]
number = input("Введите число для поиска: ")
flag = False
for i in lst:
    if number in i:
        flag = True
        break
print("Присутствует" if flag else "Не присутствует")


#2 - Найти сумму чисел списка стоящих на нечетной позиции
a = [2, 9, 5, 9, 3]
sum_odd = sum(a[item] for item in range(1, len(a), 2))
odd_el = str([a[item] for item in range(1, len(a), 2)]).strip('[]')
print(sum_odd)


#6 - Сформировать список из N членов последовательности
from random import randint

def get_degree(n):
    return [((-3)**i) for i in range(n)]

n = randint(1, 20)

print (get_degree(n))

#5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = [2, 3, 4, 5, 6]
mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

#3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)
firstPoint= list(map(int, input("Введите координаты первой точки x y z через пробел (например:  2 3 4):").split()))
secondPoint= list(map(int, input("Введите координаты второй точки x y z через пробел (например:  2 3 4):").split()))
result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] - firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
print(f"Расстояние между двумя точками пространства = {round(result, 2)}")

#4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
test_list = []
print(f"список: {test_list}")
test_item = input("Введите искомую строку: ")


def check_list(test_list, test_item):
    count = 0
    for i in range(len(test_list)):
        if test_list[i] == test_item:
            count += 1
            if count == 2:
                return i
    else:
        return -1


print(f"ответ: {check_list(test_list, test_item)}")

