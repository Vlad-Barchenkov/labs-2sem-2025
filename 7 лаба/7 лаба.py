# #1
# import random
#
# spisok = [random.randint(1, 10) for a in range(5)]
# chisl_user = int(input("Введите любое число от 1 до 10, проверим вашу удачу: "))
# if chisl_user in spisok: print(f"Список - {spisok} \nВаше число - {chisl_user} \nПоздравляю, Вы угадали число!")
# else: print(f"Список - {spisok} \nВаше число - {chisl_user} \nНет такого числа!")

# #2
# spisok = []
# previous_value = ()
# res = set()
#
# for a in range(7):
#     chisl_user = int(input("Введите число: "))
#     spisok.append(chisl_user)
# sort_spisok = sorted(spisok)
# print(sort_spisok)
#
# for i in sort_spisok:
#     if i == previous_value: res.add(i)
#     else: previous_value = i
#
# if res: print("Повторяющиеся цифры:", list(res))
# else: print("Я не нашёл повторяющихся цифр(")
#
# #3
# dni_nedeli = ('Понедельник,', 'Вторник,', 'Среда,', 'Четверг,', 'Пятница,', 'Суббота,', 'Воскресенье.')
# res_user = int(input("Сколько выходных на неделе вы хотите? - "))
#
# print(f"Ваши рабочие дни: {' '.join(dni_nedeli[:(7 - res_user)])}")
# print(f"Ваши выходные дни: {' '.join(dni_nedeli[(7 - res_user):])}")
#
# #4
# import random
#
# spisok1 = ["Алексеев", "Барченков", "Горбачёва", "Коробейникова", "Никулин", "Фараджева", "Муаммадиев", "Кузнецов", "Шевченко", "Попова"]
# spisok2 = ["Авдеев", "Базис", "Воландеморт", "Гагарина", "Иванов", "Рубик", "Фаррахов", "Чайковский", "Шарафеев", "Юрченко"]
#
# rnd_spisok1 = random.sample(spisok1, 5)
# rnd_spisok2 = random.sample(spisok2, 5)
# rnd_sport = rnd_spisok1 + rnd_spisok2
# sport = tuple(rnd_sport)
#
# print(f"Первая группа: {' '.join(rnd_spisok1)}")
# print(f"Вторая группа: {' '.join(rnd_spisok2)}")
# print("Общая спортивная группа:", *sport)
#
# print(f"Длина команды: {len(sport)}")
#
# stroke = list(sport)
# sort_sport = sorted(stroke)
# print("Отсортированная по алфавиту команда:", ' '.join(sort_sport))
#
# check = "Иванов"
# c = sort_sport.count(check)
#
# if check in sort_sport: print(f"Фамилия (Иванов) встречается в списке {c} раз")
# else: print("Фамилия (Иванов) ни разу не встретилась в списке")