from random import randint


class Rul:

    def __init__(self):
        self.reds = (1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36)
        self.blacks = (2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35)

    def roll(self):
        n = randint(0, 36)
        # print(n)

        isdigit = False
        user_n = input('>> Введите число или цвет:  ')

        if user_n.isdigit():
            user_n = int(user_n)
            isdigit = True
        elif user_n not in ['black', 'red']:
            return None

        red = False
        black = False

        if n == 0:
            print('zero')
        elif n in self.reds:
            print(n, 'красное')
            red = True
        elif n in self.blacks:
            print(n, 'черное')
            black = True

        if isdigit:
            if n == user_n:
                return 'Ok'
            return 'Вы проиграли'
        else:
            if user_n == 'red' and red:
                return 'Ok'
            elif user_n == 'black' and black:
                return 'Ok'
            return 'Вы проиграли'


r = Rul()
print(r.roll())