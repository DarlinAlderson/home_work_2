# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Например, Петя загадал числа 5 и 2. Их умма будет равна 7, а их произведение равно 10.

print("Программа выдаст 2 числа, которые были задуманы Петей, зная их сумму и произведение. ")

x = int(input("Введите сумму задуманных чисел: "))
y = int(input("Введите произведение задуманных чисел: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(f"Петя загадал числа: {i} и {j}")