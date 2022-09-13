#1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [2, 3, 5, 9, 3]
def summa(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        sum = sum + lst[i]
    print(sum)
summa(lst)      

#2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если остается 1 элемент без пары - умножаем его самого на себя.

lst = [2, 3, 4, 5, 6]
def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)
mult_lst(lst)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
def func(lst):
    min = 1
    max = 0
    for i in lst:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)  
    print(max-min)
func(lst)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num = int(input("Введите число:\n"))
def func(num):
    x = ""
    while num != 0:
        x = str(num%2) + x
        num //=2
    print(x)
func(num)

#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2
list = [0]
userNumber = int(input('Введите число: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)