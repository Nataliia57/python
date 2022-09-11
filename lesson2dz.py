# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными        

num = str(input("Введите число: "))
sum = 0
for i in num:
    if i.isdigit():
        sum += int(i)
print(sum)

#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
n = int(input('Введите число N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

#3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".

n = int(input("Введите число проверка палиндром:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("Это палиндром!")
else:
    print("Это не палиндром!")

#4 - Реализуйте выдачу случайного числа
import random
from datetime import datetime, timedelta
min_year=1886
max_year=datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year+1
end = start + timedelta(days=365 * years)

for i in range(10):
    random_date = start + (end - start) * random.random()
    print(random_date)

