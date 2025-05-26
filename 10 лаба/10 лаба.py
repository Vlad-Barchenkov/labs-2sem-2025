import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# #1
# def crop_image(input_file, output_file, left, top, right, bottom):
#     img = Image.open(input_file)
#     crop_img = img.crop((left, top, right, bottom))
#     crop_img.save(output_file)
#
# input_file = os.path.join("ЛР10", "ОТКРЫТКА.jpg")
# output_file = os.path.join("ЛР10", "ОТКРЫТКА_ОБРЕЗАННАЯ.jpg")
#
# crop_image(input_file, output_file, 20, 20, 100, 100)

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
# if vvod_p in prazdn:
#     image = prazdn[vvod_p]
#     print(f"Открытка к празднику '{vvod_p}':")
#     try:
#         img = Image.open(os.path.join("ЛР10", f"{prazdn[vvod_p]}"))
#         img.show()
#     except FileNotFoundError:
#         print(f"Файл '{image}' не найден")
# else:
#     print(f"Открытка к празднику '{vvod_p}' не найдена")

#3
prazdn = {"день рождения" : "ДР.jpg",
          "новый год" : "НГ.jpeg",
          "день пива" : "ДП.jpg",
          "8 марта" : "8МАРТА.webp",
          "23 февраля" : "23ФЕВРАЛЯ.jpeg",
          "9 мая" : "9МАЯ.jpg",
          "пасха" : "ХВ.jpg",}

vvod_p = input("К какому празднику вам нужна открытка? \n").lower()
name_user = input("Кого вы хотите поздравить? \n")

def add_name(img):
    draw = ImageDraw.Draw(img)
    name_text = f"{name_user}, поздравляю!"
    font = ImageFont.truetype("./SignateGrotesk-Black.ttf", 70)
    bbox = draw.textbbox((0, 0), name_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) // 2
    y = img.height - text_height - 100
    draw.text((x, y), name_text, font=font, fill=(250, 250, 255))
    return img

if vvod_p in prazdn:
    image = prazdn[vvod_p]
    print(f"Открытка к празднику '{vvod_p}':")
    try:
        img = Image.open(os.path.join("ЛР10", f"{prazdn[vvod_p]}"))
        name_user_img = add_name(img)
        os.makedirs("ЛР9", exist_ok=True)
        name_user_img.save(os.path.join("ЛР10", f"{prazdn[vvod_p]}.png"))
        name_user_img.show()
    except FileNotFoundError:
        print(f"Файл '{image}' не найден")
else:
    print(f"Открытка к празднику '{vvod_p}' не найдена")