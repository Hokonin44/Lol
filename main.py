while True:
    n = input('Что будем делать (-, +, /, *): ')
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    if n == "+":
        r = a + b
        print(r)
    elif n == '-':
        r = a - b
        print(r)
    elif n == '*':
        r = a * b
        print(r)
    try:
        if n == '/':
            r = a / b
            print(r)
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
        continue


