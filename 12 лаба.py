# #1
# import json
#
# def main_products():
#     with open("products.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     products = data["products"]
#
#     for product in products:
#         name = product.get("name")
#         price = product.get("price")
#         available = product.get("available")
#         weight = product.get("weight")
#
#         available_str = "В наличии" if available else "Нет в наличии!"
#
#         print(f"Название: {name}")
#         print(f"Цена: {price}")
#         print(f"Вес: {weight}")
#         print(available_str)
#         print()
#
# if __name__ == "__main__":
#     main_products()

# #2
# import json
#
# def read_products(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         data = json.load(file)
#     return data
#
#
# def write_products(filename, data):
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# def print_products(data):
#     for product in data.get("products", []):
#         name = product.get("name")
#         price = product.get("price")
#         available = product.get("available")
#         weight = product.get("weight")
#
#         availability_str = "В наличии" if available else "Нет в наличии!"
#
#         print(f"Название: {name}")
#         print(f"Цена: {price}")
#         print(f"Вес: {weight}")
#         print(availability_str)
#         print()
#
#
# def add_product_interactively(data):
#     name = input("Введите название продукта: ")
#
#     while True:
#         try:
#             price = int(input("Введите цену продукта: "))
#             break
#         except ValueError:
#             print("Цена должна быть числом. Попробуйте снова.")
#
#     while True:
#         try:
#             weight = int(input("Введите вес продукта: "))
#             break
#         except ValueError:
#             print("Вес должен быть числом. Попробуйте снова.")
#
#     avail_input = input("Продукт в наличии? (да/нет): ").strip().lower()
#     available = True if avail_input in ("да") else False
#
#     new_product = {
#         "name": name,
#         "price": price,
#         "available": available,
#         "weight": weight
#     }
#     data["products"].append(new_product)
#
#
# def main():
#     filename = "products.json"
#     data = read_products(filename)
#
#     while True:
#         answer = input("Хотите добавить новый продукт? (да/нет): ").strip().lower()
#         if answer == "да":
#             add_product_interactively(data)
#         elif answer == "нет":
#             break
#         else:
#             print("Пожалуйста, введите да или нет")

#3
import re

def create_ru_en_dict(input_filename, output_filename):
    ru_en = {}

    with open(input_filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = re.split(r"\s*[-–]\s*", line)
            if len(parts) != 2:
                print(f"Строка пропущена, т.к. не соответствует формату: {line}")
                continue

            english, russian = parts

            russian_words = [word.strip() for word in russian.split(",")]
            for ru_word in russian_words:
                if ru_word not in ru_en:
                    ru_en[ru_word] = []
                if english not in ru_en[ru_word]:
                    ru_en[ru_word].append(english)
    sorted_ru = sorted(ru_en.keys(), key=lambda x: x.casefold())

    with open(output_filename, "w", encoding="utf-8") as out_file:
        for ru_word in sorted_ru:
            english_list = ", ".join(ru_en[ru_word])
            out_file.write(f"{ru_word} – {english_list}\n")

def main():
    input_filename = "en-ru.txt"
    output_filename = "ru-en.txt"

    create_ru_en_dict(input_filename, output_filename)
    print(output_filename, "успешно сохранён")

if __name__ == "__main__":
    main()