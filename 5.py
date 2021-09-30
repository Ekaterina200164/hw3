import sys
print('Введите a и b:')
try:
    a = int(input())
    b = int(input())
    c = a//b
except ZeroDivisionError:
    print('!Деление на 0!')
except:
    print('Ошибка')
else:
    print('Результат вычислений: a//b = ', c)
finally:
    print('Работа завершена')

