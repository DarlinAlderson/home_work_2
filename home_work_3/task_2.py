# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
import time
print("Программа принимает два числа и выводит результат их деления. ")
time.sleep(1)
def div (x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
print(f"Результат деления: ", div(int(input("Введите первое число: ")), int(input("Введите второе число: "))))