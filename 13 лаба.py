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
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана {self.restaurant_name}: {self.rating}")


#13.1
print("---- Задача 13.1 ----")
newRestaurant = Restaurant("Клод Моне", "Французская", rating=4.5)

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

#13.2
print("\n---- Задача 13.2 ----")
restaurant1 = Restaurant("Пармезано", "Итальянская", rating=4.7)
restaurant2 = Restaurant("ЁбиДоЁби", "Японская", rating=4.9)
restaurant3 = Restaurant("Мак Шнакедс", "Американская", rating=4.2)

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()

#13.3
print("\n---- Задача 13.3 ----")
restaurant1.update_rating(4.8)
restaurant2.update_rating(5.0)
restaurant3.update_rating(4.3)