from random import randint

class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]  # Мешок с бочками.
        self.card = [__class__.gen_string(bag),
                     __class__.gen_string(bag),
                     __class__.gen_string(bag)] # карточка из 3х строк
        self.name = name
        self.count_barrel = 15  # осталось бочек на карточке

    @staticmethod
    def gen_string(bag): # Генерируем строку из чисел
        string = ['' for _ in range(9)] # генерируем строку из пустых ячеек
        for x in range(8, 3, -1): # для 5ти элементов
            digit = randint(0, x)  # Номер элемента строки, который заполняю
            while string[digit] != '':  # если элемент уже не пустой то переходим к следующему
                digit += 1
            string[digit] = bag.pop(randint(0, len(bag) - 1)) # убираем номера которые уже добавили на карточки
        return string

    def __str__(self): # делаем картучку и выводим ее в строковом испольнении
        sc = '{:-^26}\n'.format(self.name) # форматируем типа --- слово ---
        for x in range(3):
            sc += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return sc + '--------------------------'

computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [x for x in range(1, 91)]  # Мешок с бочками. Новый мешок, для игры от 1 до 90
while True: # Запуск игры
    if len(bag) < 1:
        print('Бочёнки в мешке закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(computer.count_barrel, player.count_barrel))
        break

    barrel = bag.pop(randint(0, len(bag) - 1)) # Вытаскиваем бочонок
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
    print(computer)
    print(player)
    reply = input('Зачеркнуть цифру? (y/n/q)')
    reply = reply.lower() # преобразуем на всякий случай, вдруг капс включен

    while len(reply) == 0 or reply not in 'ynq': # введен не правильынй символ
        print('\n\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q':
        print('Вы вышли из игры.')
        break
    elif reply == 'y':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3): # по строчно проверяем карточки [[x=1],[x=2],[x=3]]
            if barrel in player.card[x]:
                test = True
                player.card[x][player.card[x].index(barrel)] = '-' # Если совпало то вычеркиваем
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print('Вы Выиграли!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3): # по строчно проверяем карточки
            if barrel in player.card[x]:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                test = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print('Вы Выиграли!')
            break
        elif computer.count_barrel < 1:
            print('Компьютер Выиграл!')
            break