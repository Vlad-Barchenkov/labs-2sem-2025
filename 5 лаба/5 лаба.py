# #1
# n = int(input("Сколько слов вы хотите ввести?   "))
# spisok = []
#
# for i in range(n):
#     word = input(f"Введите слово №{i+1}: ")
#     spisok.append(word)
#
# res = ' '.join(spisok)
# print(res)

# #2
# n = 100**100
# spisok = []
#
# for i in range(n):
#     word = input(f"Введите слово №{i+1}: ")
#     if (word == "стоп") or (word == "Стоп") or (word == "СТОП"):
#         break
#     spisok.append(word)
#
# res = ' '.join(spisok)
# print(res)

# #3
# word = input("Введите любое русское слово: ").lower()
# ff = 0
#
# for letter in word:
#     if letter == 'ф':
#         ff = 1
#         break
#
# if ff == 1: print("Ого! Это редкое слово!")
# else: print("Эх, это не очень редкое слово...")

# #4
# import random
#
# print("Братишка, сделаешь 3 ошибки, винда удалится))) Удачной игры!")
# k = 0
# c = 0
# while True:
#     a = random.randint(1, 11)
#     b = random.randint(1, 11)
#     result = int(input(f"{a} + {b} = "))
#     if a + b == result:
#         print("Правильно!")
#         k+=1
#     elif a + b != result:
#         print("Ответ неверный")
#         c+=1
#         if c == 3:
#             break
#
# print(f"Игра окончена, винда не удалится. Правильных ответов: {k}")