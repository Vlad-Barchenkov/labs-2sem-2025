import re
import tkinter as tk
from tkinter import messagebox

# Базовый класс ресторана из предыдущих заданий
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг ресторана: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана '{self.restaurant_name}' установлен в {self.rating}")


# 14.1 и 14.2: Определяем класс IceCreamStand, наследуемый от Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating=0, location="Не указано", working_hours="Не указано",
                 flavors=None):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.location = location
        self.working_hours = working_hours
        self.flavors = flavors if flavors is not None else []
        self.popsicle_flavors = []  # Мороженое на палочке
        self.soft_serve_flavors = []  # Мягкое мороженое

    def display_flavors(self):
        if self.flavors:
            print("Доступные сорта мороженого:")
            for flavor in self.flavors:
                print(" -", flavor)
        else:
            print("Сортов мороженого нет.")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт '{flavor}' добавлен")
        else:
            print(f"Сорт '{flavor}' уже существует")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удалён")
        else:
            print(f"Сорт '{flavor}' не найден")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен")
        else:
            print(f"Сорт мороженого '{flavor}' отсутствует")

    def add_popsicle_flavor(self, flavor):
        if flavor not in self.popsicle_flavors:
            self.popsicle_flavors.append(flavor)
            print(f"Сорт мороженого на палочке '{flavor}' добавлен")
        else:
            print(f"Сорт мороженого на палочке '{flavor}' уже существует")


    def remove_popsicle_flavor(self, flavor):
        if flavor in self.popsicle_flavors:
            self.popsicle_flavors.remove(flavor)
            print(f"Сорт мороженого на палочке '{flavor}' удалён")
        else:
            print(f"Сорт мороженого на палочке '{flavor}' не найден")


    def show_popsicle_flavors(self):
        if self.popsicle_flavors:
            print("Сорта мороженого на палочке:")
            for flavor in self.popsicle_flavors:
                print(" -", flavor)
        else:
            print("Нет сортов мороженого на палочке")


    def add_soft_serve_flavor(self, flavor):
        if flavor not in self.soft_serve_flavors:
            self.soft_serve_flavors.append(flavor)
            print(f"Сорт мягкого мороженого '{flavor}' добавлен")
        else:
            print(f"Сорт мягкого мороженого '{flavor}' уже существует")


    def remove_soft_serve_flavor(self, flavor):
        if flavor in self.soft_serve_flavors:
            self.soft_serve_flavors.remove(flavor)
            print(f"Сорт мягкого мороженого '{flavor}' удалён")
        else:
            print(f"Сорт мягкого мороженого '{flavor}' не найден")


    def show_soft_serve_flavors(self):
        if self.soft_serve_flavors:
            print("Сорта мягкого мороженого:")
            for flavor in self.soft_serve_flavors:
                print(" -", flavor)
        else:
            print("Нет сортов мягкого мороженого")


    def describe_ice_cream_stand(self):
        self.describe_restaurant()
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")


# 14.3: Создаем графический интерфейс с использованием tkinter для IceCreamStand.
class IceCreamStandGUI:
    def refresh_flavors_listbox(self):
        self.flavors_listbox.delete(0, tk.END)
        for flavor in self.ice_cream_stand.flavors:
            self.flavors_listbox.insert(tk.END, flavor)

    def add_flavor(self):
        flavor = self.new_flavor_entry.get().strip()
        if flavor:
            self.ice_cream_stand.add_flavor(flavor)
            self.new_flavor_entry.delete(0, tk.END)
            self.refresh_flavors_listbox()
        else:
            messagebox.showwarning("Внимание", "Введите название сорта мороженого!")

    def remove_flavor(self):
        selected_indices = self.flavors_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            flavor = self.flavors_listbox.get(index)
            self.ice_cream_stand.remove_flavor(flavor)
            self.refresh_flavors_listbox()
        else:
            messagebox.showwarning("Внимание", "Выберите сорт мороженого для удаления!")

    def check_flavor(self):
        flavor = self.check_flavor_entry.get().strip()
        if flavor:
            if flavor in self.ice_cream_stand.flavors:
                messagebox.showinfo("Результат", f"Сорт мороженого '{flavor}' доступен")
            else:
                messagebox.showinfo("Результат", f"Сорт мороженого '{flavor}' отсутствует")
        else:
            messagebox.showwarning("Внимание", "Введите название сорта мороженого для проверки!")

    def __init__(self, ice_cream_stand):
        self.ice_cream_stand = ice_cream_stand

        self.window = tk.Tk()
        self.window.title("Кафе Мороженого")

        # Фрейм для общей информации (название, локация, время работы)
        info_frame = tk.Frame(self.window)
        info_frame.pack(pady=10)

        self.info_label = tk.Label(
            info_frame,
            text=(f"{self.ice_cream_stand.restaurant_name}\n"
            f"Локация: {self.ice_cream_stand.location}\n"
            f"Время работы: {self.ice_cream_stand.working_hours}"),
            font=("Arial", 14)
        )
        self.info_label.pack()

        self.flavors_listbox = tk.Listbox(self.window, width=50)
        self.flavors_listbox.pack(pady=10)
        self.refresh_flavors_listbox()

        # Фрейм для ввода нового сорта
        entry_frame = tk.Frame(self.window)
        entry_frame.pack(pady=5)

        tk.Label(entry_frame, text="Новый сорт мороженого:").pack(side=tk.LEFT)
        self.new_flavor_entry = tk.Entry(entry_frame)
        self.new_flavor_entry.pack(side=tk.LEFT)

        # Фрейм с кнопками для добавления и удаления сорта
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=5)

        add_button = tk.Button(button_frame, text="Добавить сорт", command=self.add_flavor)
        add_button.pack(side=tk.LEFT, padx=5)

        remove_button = tk.Button(button_frame, text="Удалить выбранный сорт", command=self.remove_flavor)
        remove_button.pack(side=tk.LEFT, padx=5)

        # Фрейм для проверки наличия сорта
        check_frame = tk.Frame(self.window)
        check_frame.pack(pady=5)

        tk.Label(check_frame, text="Проверить наличие сорта:").pack(side=tk.LEFT)
        self.check_flavor_entry = tk.Entry(check_frame)
        self.check_flavor_entry.pack(side=tk.LEFT)
        check_button = tk.Button(check_frame, text="Проверить", command=self.check_flavor)
        check_button.pack(side=tk.LEFT, padx=5)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    # 14.1 и 14.2: Создаем экземпляр кафе мороженого
    ice_cream_cafe = IceCreamStand(
        "ICEКРЕМ",
        "Мороженка",
        rating=4.8,
        location="г.Санкт-Петербург, Валдайская, 6к1",
        working_hours="10:00 - 22:00",
        flavors=["Шоколадное", "Ванильное", "Клубничное"]
    )

    print("=== Описание кафе мороженого ===")
    ice_cream_cafe.describe_ice_cream_stand()
    print()
    ice_cream_cafe.display_flavors()
    print()

    ice_cream_cafe.add_flavor("Мятное")
    ice_cream_cafe.check_flavor("Мятное")
    ice_cream_cafe.remove_flavor("Клубничное")
    print()
    ice_cream_cafe.display_flavors()
    print()

    ice_cream_cafe.add_popsicle_flavor("Лимонное")
    ice_cream_cafe.show_popsicle_flavors()

    # 14.3: Запуск графического интерфейса для кафе мороженого
    gui = IceCreamStandGUI(ice_cream_cafe)
    gui.run()