# # Практика 

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
#     def display_info(self):
#         print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")
        
# # car = Car("Toyota", 'Corolla', 2020)
# # car.display_info()

# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_capacity):
#         super().__init__(brand, model, year)
#         self.battery_capacity = battery_capacity
        
#     def display_battery_info(self):
#         print(f'Емкость батареи: {self.battery_capacity} kWh')
        
# car = ElectricCar("Tesla", "Model S", 2021, 100)
# car.display_info()
# car.display_battery_info()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = 0
        
    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")
        
    def set_mileage(self, mileage):
        self.__mileage = mileage
        
    def get_mileage(self):
        return self.__mileage
    
car = Car("Toyota", 'Corolla', 2020)
car.set_mileage(15000)
print(f"Пробег: {car.get_mileage()} км")
        
        
class Dog:
    def make_sound(self):
        print("woof")
        
class Cat:
    def make_sound(self):
        print("meow")
        
# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.make_sound()

# dog = Dog()
# cat = Cat()

# dog.make_sound()
# cat.make_sound()

import time
