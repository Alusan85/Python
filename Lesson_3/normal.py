# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Задача - 1")
def fibonacci(n, m):
    a = 1
    b = 1
    fibo = []
    for z in range(2,m+1):
        c = a + b
        a, b = b, c
        if (z >= n)&(z<=m): # c элемента (если от него и дальше заменить => на >)
            fibo.append(a)
    return fibo

print(fibonacci(5, 10))
print(fibonacci(10, 18))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print("Задача - 2")
def sort_to_max(origin_list):
    leng = len(origin_list)

    for i in range(0,leng-1):
        for j in range (0,leng-i-1):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j],origin_list[j+1] = origin_list[j+1],origin_list[j]
    print(origin_list)
            
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# filter(function, iterable)
# Возвращает итератор из тех элементов, для которых function возвращает истину.
print("Задача - 3")
def filter_raw(func, itr):
   
    new_itr = [elem for elem in itr if func(elem)]

    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)

    print(new_itr)
    return new_itr

filter_raw(lambda x: x < 5, {2, 10, -12, 2.5, 20, -11, 4, 4, 0})
filter_raw(lambda x: x < 5, [2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Задача - 4")
import math
A1, A2, A3, A4 = (1, 3), (4, 7), (2, 8), (-1, 4)

def isParallel(a, b, c, d):
    '''
    Проверка признаков параллелограмма
    Задаем переменные чтобы проверить несколько возможных вариантов
    1 - Что стороны равны и параллельны
    2 - Диагонали деляться в точке пересечения пополам
    '''
    p1 = False
    p2 = False
    '''
    Противополжные стороны параллельны и равны
    формулу подсмотреть можно на https://znanija.com/task/5609424
    Вычисляем каждую сторону параллелограмма и проверяем длины
    '''
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    bс = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)

    if ab == cd and bс == ad:
        print("Равенство сторон: верно")
        p1 = True
    else:
        print("Противоположные стороны не равны")
    '''
    Диагонали D1 и D2 в точках пересечения делятся пополам и равны
    '''
# ( (x1 + x2)/2; (y1 + y2)/2 ) - формула для вычесления

    diag_half_1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    diag_half_2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)

    if diag_half_1 == diag_half_2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей не равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s\nОбразуют параллелограмм' %
              (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

isParallel(A1, A2, A3, A4)
