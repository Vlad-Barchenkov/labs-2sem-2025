# #1
# def func(n):
#     if n % 3 == 0: print("Число делится на 3, Братик")
#     else: print("Число не делится на 3 (((")
#
# x = int(input("Введи любое число: "))
# func(x)

# #2
# def func():
#     try:
#         chsl=int(input("Введите число: "))
#         res=100/chsl
#         print(f"100 / {chsl} = {res}")
#     except ValueError:
#         print("Напиши внатуре число да")
#     except ZeroDivisionError:
#         print("Ты че дурачок? На 0 делить нельзя, если ты конечно не учился в СПбГУПТД")
# func()

# #3
# from datetime import datetime
# def func(n):
#     try:
#         date = datetime.strptime(n,"%d.%m.%Y")
#         day = date.day
#         month = date.month
#         year = date.year
#         if day * month == year % 100:
#             return True
#         else:
#             return False
#     except ValueError:
#         print("Введите дату в формате (дд.мм.гггг.): ")
#
# vvod_usera = input("Введите дату: ")
# if func(vvod_usera) == True:
#     print("Дата является магической")
# else:
#     print("Дата не является магической")

# #4
# def func(sm):
#     if len(sm) % 2 != 0:
#         print("Введите билет, чтобы количество цифр было чётным")
#         return
#
#     half = len(sm) // 2
#     del1 = sum(map(int, sm[:half]))
#     del2 = sum(map(int, sm[half:]))
#     if del1 == del2: print("Это счастливый билет")
#     else: print("Это не счастливый билет")
#
# Z = input("Введите номер лотерейного билета: ")
# func(Z)