#1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
i = 2 # первое простое число
a = []
b = num
while i <= num:
    if num % i == 0:
        a.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {b} приведены в списке: {a}")

#2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
x = list(map(int, input("Задайте последовательность чисел через пробел:\n").split()))
print(f"список чисел: {x}")
y = []
[y.append(i) for i in x if i not in y]
print(f"Список из неповторяющихся элементов: {y}")

#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
studs = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    sname = input(str(i+1) + "-й студент: ")
    point = int(input("Балл: "))
    studs[sname] = point
    s += point
 
avrg = s / n
print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
for i in studs:
    if studs[i] > avrg:
        print(i)

#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
print("Шифр Цезаря")
s = "Hello world!"


def caesar_encode(mes, z):
    return [chr((ord(i) + z) % 65536) for i in mes]


def caesar_decode(mes, z):
    return [chr((65536 + (ord(i) - z) % 65536) % 65536) for i in mes]


a = caesar_encode(s, 10)
b = caesar_decode(a, 10)
print(s, a, "".join(b))

print("Взлом шифра цезаря")


def caesar_hack(mes):
    numdict = {}
    for i in set(mes):
        numdict[i] = mes.count(i)
    chmax = max(numdict.values())
    plist = []
    for k, v in numdict.items():
        if v == chmax:
            plist.append(k)
    for ch in plist:
        yield [chr((65536 + (ord(i) - (ord(ch) - ord(" ")) % 65536)) % 65536)
               for i in mes]


print(*[''.join(i) for i in list(caesar_hack(a))], sep="\n")

#5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Декодированная строка: \t' + decoded_string)
print('Закодированная строка: \t' + rle_encode(decoded_string))
print(f'Коэффициент сжатия: \t{round(len(decoded_string) / len(encoded_string), 1)}')