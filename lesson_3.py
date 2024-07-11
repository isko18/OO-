# ООП - принцип Абстракции 
from abc import ABC, abstractmethod

# # Абстрактный класс
# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass 
    
# # Конкретный класс для обработки платежей 
# class CreditCardPayment(Payment):
#     def process_payment(self, amount):
#         return print(f"Оплата произведена по Кредитной карте, на сумму {amount}$ ")

# # Конкретный класс для обработки платежей 
# class PayPalPayment(Payment):
#     def process_payment(self, amount):
#         return print(f'Оплата произведена по PayPal, на сумму {amount}$')

# #Функция для принятия платежей 
# def make_payment(payment_method, amount):
#     payment_method.process_payment(amount)

# #Создаем объект разных видов платежей 
# credit_card_payment = CreditCardPayment()
# paypal = PayPalPayment()

# # Выполняем плтежи
# make_payment(credit_card_payment, 100)
# make_payment(paypal, 200)

# class Pet(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass 
    
# class Dog(Pet):
#     def make_sound(self):
#         print("Woof")
        
# class Cat(Pet):
#     def make_sound(self):
#         print("Meow")

# def play_with_pet(pet):
#     pet.make_sound()
    
# dog = Dog()
# cat = Cat()

# print("Игарть с собакой: ")
# play_with_pet(dog)

# print("Играть с кошкой: ")
# play_with_pet(cat)

# Полиморфизм

# class Cat:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
        
#     def info(self):
#         print(f"Я кошка. Меня зовут {self.name}. Мне {self.age} годика")
        
#     def make_sound(self):
#         print("Meow")
        
# class Dog:
#         def __init__(self, name, age):
#             self.name = name 
#             self.age = age 
        
#         def info(self):
#             print(f"Я собака. Меня зовут {self.name}. Мне {self.age} годика")
        
#         def make_sound(self):
#             print("Woof")
            
# cat1 = Cat('Мурка', 2)
# dog1 = Dog('Ak-tosh', '4')

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name 
        
    def area(self):
        pass 
    
    def fact(self):
        return "Я двуменая фигура"
    
    def __str__(self):
        return self.name
    
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    
    def area(self):
        pass 
    
    def fact(self):
        return "У квадрата каждый угол равен 90 градусам"       
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def area(self):
        return pi*self.radius**2
    
a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())




                           # public
 #Инкапсуляция               protected
                           # private 