# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

import time

print("Программа принимает принимает три позиционных аргумента и возвращает сумму наибольших двух. ")
time.sleep(1)
print("Var_1")


def my_func(arg1, arg2, arg3):
    print(f'Сумма наибольших двух аргументов: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')))


time.sleep(1)
print("Var_2")

args = (
    int(input('Введите первый аргумент: ')),
    int(input('Введите второй аргумент: ')),
    int(input('Введите третий аргумент: ')))

print(sorted(args, reverse=True))
args_1 = sorted(args, reverse=True)


def sum(args_1):
    return args_1[0] + args_1[1]


print(f'Сумма наибольших двух аргументов: {sum(args_1)}')