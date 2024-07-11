#   Инкапсуляция

# Публичный
# class PublicExample:
#     def __init__(self, value):
#         self.value = value # Публичный атрибут 
        
#     def info(self):
#         return self.value # Публичный метод
    
# public = PublicExample(42)

# print(public.info()) # Вызов публичный метод 
# print(public.value) # Доступ к публичному атрибуту 

# Защищенный

# class ProtectedExample:
#     def __init__(self, value):
#         self._value = value # Защищенный атрибут 
        
#     def _info(self):
#         return self._value # Защищенный метод
    
# protected = ProtectedExample(43)
# print(protected._value)
# print(protected._info())

# # Приватный 

# class PrivateExample:
#     def __init__(self, value):
#         self.__value = value # Приватный атрибут
        
#     def __info(self):
#         return self.__value # Приватный метод
    
#     def access_private(self):
#         return self.__info() # Публичный метод, где мы получаем доступ к приватному атрибуту 
            
        
# private = PrivateExample(55)
 # Прямой доступ к приватному атрибуту вызовет ошибку
# print(private.__value)

 # Прямой вызов приватного метода вызовет ошибку  
# print(private.__info()) 

# Доступ через публичный метод
# print(private.access_private())

# Доступ к приватному атрибуту через name mangling
# print(private._PrivateExample__value)

# class Example(PrivateExample):
#     def __init__(self, value, current):
#         super().__init__(value)
#         self._current = current

#     def public(self):
#         print(f'Приватный - {self.access_private()}, Защищенный {self._current}')

# example = Example(3, 5)
# print(example.public())

# print(private.access_private())
# print(private._PrivateExample__value)
import datetime

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self._year = year
        self.__mileage = mileage
        
    def display_info(self):
        print(f'Марка: {self.make}, \nМодель: {self.model}')
        
    def _calculate_age(self):
        current = datetime.datetime.now().year
        return current - self._year
    
    def  __update_mileage(self):
        print(self.__mileage)
            
    def  set_mileage(self):
        return self.__update_mileage()
    
car = Car("Mazda", "RX8", 2015, 2000)

print(car.make)
print(car.model)
print(car._year)  # Доступ к защищенным атрибутам и методам (не рекомендуется)

# print(car.__mileage) # Доступ по атрибуту ограничен.

# car.__update_mileage(600)  # Доступ к приватным атрибутам и методам (прямой доступ вызовет ошибку)

print(car.set_mileage())

print(car._Car__mileage) # Доступ к приватному атрибуту через name mangling