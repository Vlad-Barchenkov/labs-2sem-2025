import random
import os
from random import randint

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# #1
# img = Image.open(os.path.join("ЛР9", "ЛР9.1.jpg"))
# img.show()
# print(f"Размер изображения: {img.width} х {img.height} \nФормат изображения: {img.format} \nЦветовая модель изображения: {img.mode}")

# #2
# img = Image.open(os.path.join("ЛР9", "ЛР9.1.jpg"))
# res_img = img.resize((img.width // 3, img.height // 3))
# os.makedirs("ЛР9", exist_ok=True)
# res_img.save(os.path.join("ЛР9", "ЛР9.2 - res.jpg"))
# hor_img = res_img.transpose(Image.FLIP_LEFT_RIGHT)
# os.makedirs("ЛР9", exist_ok=True)
# hor_img.save(os.path.join("ЛР9", "ЛР9.2 - hor.jpg"))
# ver_img = res_img.transpose(Image.FLIP_TOP_BOTTOM)
# os.makedirs("ЛР9", exist_ok=True)
# ver_img.save(os.path.join("ЛР9", "ЛР9.2 - ver.jpg"))

# #3
# # filtr = {
# #         "SHARPEN": ImageFilter.SHARPEN,
# #          "CONTOUR": ImageFilter.CONTOUR,
# #          "UnsharpMask": ImageFilter.UnsharpMask,
# #          "SMOOTH": ImageFilter.SMOOTH,
# #          "SMOOTH_MORE": ImageFilter.SMOOTH_MORE
# # }
# #
# # selected_filtr = filtr["SMOOTH"]
# #
# # for i in range(1, 6):
# #     img = Image.open(os.path.join("ЛР9", f"{i}.jpg"))
# #     filtered_img = img.filter(selected_filtr)
# #     filtered_img.save(f"ЛР9.3.{i}.jpg")
#
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
#     img = Image.open(os.path.join("ЛР9", f"{i}.jpg"))
#     filtered_img = img.filter(selected_filtr)
#     os.makedirs("ЛР9", exist_ok=True)
#     filtered_img.save(os.path.join("ЛР9", f"ЛР9.3.{i}.jpg"))

# #4
# def add_watermark():
#     draw = ImageDraw.Draw(img)
#     watermark_text = "© 2025 UI.UX.VLM"
#     font = ImageFont.truetype("Montserrat.ttf", 30)
#     text_width, text_height = draw.textsize(watermark_text, font=font)
#     x = img.width - text_width - 10
#     y = img.height - text_height - 10
#     draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 60))
#     return img
#
# for i in range(1, 5):
#     img = Image.open(os.path.join("ЛР9", f"WATERMARKOFF{i}.jpg"))
#     watermark_img = add_watermark(img)
#     os.makedirs("ЛР9", exist_ok=True)
#     watermark_img.save(os.path.join("ЛР9", f"WATERMARKON{i}.jpg"))

def add_watermark(img):
    draw = ImageDraw.Draw(img)
    watermark_text = "©2025 UI.UX.VLM"
    font = ImageFont.truetype("./SignateGrotesk-Black.ttf", 100)
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = img.width - text_width - 10
    y = img.height - text_height - 30
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 60))
    return img

for i in range(1, 5):
    img = Image.open(os.path.join("ЛР9", f"WATERMARKOFF{i}.jpg"))
    watermarked_img = add_watermark(img)
    os.makedirs("ЛР9", exist_ok=True)
    watermarked_img.save(os.path.join("ЛР9", f"WATERMARKON{i}.jpg"))