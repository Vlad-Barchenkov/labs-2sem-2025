#1
#password = input("Салам братик, придумай пароль: ")
#if len(password) >= 6:
#    password2 = input("Хорош, а повтори свой пароль: ")
#    if password == password2:
#        print("Пароль принят, братик")
#    else:
#        print("Пароль не принят, братик(")
#if len(password) <= 6:
#    print("Введи пароль из 6 символов пж")

#2
#num = int(input("Братик, введи номер своего места: "))
#if 1 <= num <= 36:
#    if num % 2 == 0: print("У тебя верхнее место в купе")
#    else: print("У тебя нижнее место в купе")
#elif 37 <= num <= 54:
#    if num % 2 == 0: print("У тебя верхнее место сбоку")
#    else: print("У тебя нижнее место сбоку")
#else:
#    print("Ты че, в вагоне всего 54 места")

#3
#def oprgod(year):
#    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#        return(f"Год {year} - високосный")
#    else:
#        return("Это год не високосный")
#
#year = int(input("Введи любой год, чтобы узнать високосный он или нет: "))
#print(oprgod(year))

#4
#def Mix_color(usercvet1, usercvet2):
#    colors = ["красный", "синий", "желтый"]
#    if usercvet1 not in colors or usercvet2 not in colors:
#        return "Ошибка: Введены некорректные названия цветов, используйте 'красный', 'синий' или 'желтый'."
#    if usercvet1 == "красный" and usercvet2 == "синий" or usercvet1 == "синий" and usercvet2 == "красный":
#        return "Получился: фиолетовый"
#    elif usercvet1 == "красный" and usercvet2 == "желтый" or usercvet1 == "желтый" and usercvet2 == "красный":
#        return "Получился: оранжевый"
#    elif usercvet1 == "синий" and usercvet2 == "желтый" or usercvet1 == "желтый" and usercvet2 == "синий":
#        return "Получился: зелёный"
#    else:
#      return "Ошибка: Непредвиденная комбинация цветов."
#usercvet1 = input("Введи первый цвет для смешивания: ").lower()
#usercvet2 = input("Введи второй цвет для смешивания: ").lower()
#print(Mix_color(usercvet1, usercvet2))