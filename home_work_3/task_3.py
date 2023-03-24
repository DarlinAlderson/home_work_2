# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456
import time

print("Программа принимает данные пользователя и выводит их одной строкой. ")
time.sleep(1)


def user_data(arg_name, arg_surname, arg_year_of_birth, arg_city, arg_email, arg_phone_number):
    return f"Your name: {arg_name}, Your surname: {arg_surname}, Your year of birth: {arg_year_of_birth}, " \
           f"Your city: {arg_city}, Your email: {arg_email}, Your phone number: {arg_phone_number}"


name = input("Enter your name: ")
surname = input("Enter your surname: ")
year_of_birth = int(input("Enter your year of birth: "))
city = input("Enter your city: ")
email = input("Enter your email: ")
phone_number = int(input("Enter your phone number: "))

print(user_data(arg_name=name, arg_surname=surname, arg_year_of_birth=year_of_birth, arg_city=city, arg_email=email,
                arg_phone_number=phone_number))