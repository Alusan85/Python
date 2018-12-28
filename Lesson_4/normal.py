# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re
 
n = (random.randint(0, 9) for i in range(2500)) 
str = ''.join(str(i) for i in n) 
 
with open('test.txt', 'w')  as file: 
    file.write(str)

with open('test.txt', 'r') as file:
    result = ['0']
    longnum = file.read()
    pattern = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
    found = re.findall(pattern, longnum)
    [result.insert(0, x) for x in found if len(x) > len(result[0])]
    print(longnum)
    print(result.pop(0))

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится
# ровно один ноль на случайном месте, остальные элементы тоже рандомные.
# Пользователь вводит размер

n = int(input("Введите размер матрицы для заполнения : "))
ArrayZero = [[random.randint(0,100) for j in range(n)] for i in range(n)]

for i in range(n):
    ArrayZero[i][random.randint(0,n-1)]=0

for i in range(len(ArrayZero)):
    for j in range(len(ArrayZero[i])):
        print(f"{ArrayZero[i][j]:>3}", end=" ")
    print()




