# https://pythonworld.ru/moduli/modul-os.html  -- все команды модуля OS можно получить тут
# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# os.path.dirname(path) - возвращает имя директории пути path.
# os.getcwd() - текущая рабочая директория.
# os.listdir(path=".") - список файлов и директорий в папке.
# except WindowsError - отлавливаем ошибки в Винде, начиная с версии Py 3.3

#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys

def make_dir(name_dir):

    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')

def del_dir(name_dir):

    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
    make_dir(cur_dir)

for cur_dir in dirs:
    del_dir(cur_dir)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dir_list():

    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    return list_dir

print(dir_list())

#HARD

# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить


import os
import sys
import shutil

dir_path = input("Input path to dir: ")

if "win32" == sys.platform:
    dir_path = dir_path.replace("/", "\\")
else:
    dir_path = dir_path.replace("\\", "/")

files = os.listdir(dir_path)

exts = []
for i in files:
    if "." in i:
        exts.append(os.path.splitext(i)[1])

for i in set(exts):
    if not os.path.exists(os.path.join(dir_path, i)):
        os.mkdir(os.path.join(dir_path, i))

for file in files:
    try:
        destination = os.path.splitext(file)[1]
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, destination, file))
    except WindowsError:
        print('Что то пошло не так c перемещением файлов из корня в папки расширений')

print ("Проверь папочку, файлы ушли по своим расширениям")
input("Нажми любую клавишу...")

for root, dirs, files in os.walk(dir_path): # Вытаскиваем файлы из папки
    for file in files:
        try:
            path_file = os.path.join(root,file)
            shutil.move(path_file, dir_path)
        except WindowsError:
            print('Что то пошло не так c извлечением файлов')

for root, dirs, files in os.walk(dir_path): # Удаляем папки
   for directory in dirs:
        try:
            path_dir = os.path.join(root,directory)
            os.rmdir(path_dir)
        except WindowsError:
            print('Что то пошло не так с удалением папок')
print ("Проверь папочку, файлы снова в корневом каталоге")

