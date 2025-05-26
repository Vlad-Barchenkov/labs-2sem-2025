import random
import os
import mimetypes
from random import randint

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# #1
# filtr = {
#         "SHARPEN": ImageFilter.SHARPEN,
#          "CONTOUR": ImageFilter.CONTOUR,
#          "UnsharpMask": ImageFilter.UnsharpMask,
#          "SMOOTH": ImageFilter.SMOOTH,
#          "SMOOTH_MORE": ImageFilter.SMOOTH_MORE
# }
#
# rnd_filtr = random.choice(list(filtr.keys()))
# selected_filtr = filtr[rnd_filtr]
#
# for i in range(1, 6):
#     img = Image.open(os.path.join("ЛР11", f"{i}.jpg"))
#     filtered_img = img.filter(selected_filtr)
#     os.makedirs("ЛР11", exist_ok=True)
#     filtered_img.save(os.path.join("ЛР11", f"ЛР11.1.{i}.jpg"))

# #2
# prazdn = {"день рождения" : "ДР.jpg",
#           "новый год" : "НГ.jpeg",
#           "день пива" : "ДП.jpg",
#           "8 марта" : "8МАРТА.webp",
#           "23 февраля" : "23ФЕВРАЛЯ.jpeg",
#           "9 мая" : "9МАЯ.jpg",
#           "пасха" : "ХВ.jpg",}
#
# vvod_p = input("К какому празднику вам нужна открытка? \n").lower()
# if (vvod_p in prazdn):
#     image = prazdn[vvod_p]
#     try:
#         if image.lower().endswith(('.jpg', '.png')):
#             img = Image.open(os.path.join("ЛР10", f"{prazdn[vvod_p]}"))
#             print(f"Открытка к празднику '{vvod_p}':")
#             img.show()
#         else:
#             print("Файл имеет неподходящее расширение")
#     except FileNotFoundError:
#         print(f"Файл '{image}' не найден")
# else:
#     print(f"Открытка к празднику '{vvod_p}' не найдена")
#
# #3
# import csv
#
# def read_csv(filename):
#     data = []
#     with open(filename, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             row['Количество'] = int(row['Количество'])
#             row['Цена'] = int(row['Цена'])
#             data.append(row)
#     return data
#
# def calculate_c(data):
#     c = 0
#     for item in data:
#         c += item['Количество'] * item['Цена']
#     return c
#
# def print_shopping_list(data, c):
#     print("Нужно купить:")
#     for item in data:
#         print(f"{item['Продукт']} - {item['Количество']} шт. за {item['Цена']} руб.")
#     print(f"Итоговая сумма: {c} руб.")
#
# def main():
#     filename = 'shopping_list.csv'
#     data = read_csv(filename)
#     total = calculate_c(data)
#     print_shopping_list(data, total)
#
# # В питоне __name__ всегда равен "__main__"
# if __name__ == "__main__":
#     main()