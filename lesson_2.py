# # ооп - Наследование 

class Transport: # Родительский класс
    # wheels = 4
    def __init__(self, model, year, color):
        self.model = model 
        self.year = year
        self.color = color

    def info(self):
        print(f'Бренд транспорта - {self.model}, Год выпуска - {self.year}, Цвет - {self.color}')
        
class Car(Transport): # Дочерний класс
    def __init__(self, model, year, color, penalties = 2000):
        # Transport.__init__(self, model, year, color,) # первый способ (Напрямую к классу)
        super().__init__(model, year, color) # Второй способ (с помощю метода super() )
        self.penalties = penalties
        
lexus = Car("lx 300", 2023, 'white')
lexus.info()
print(lexus.penalties)


class Animals:
    def __init__(self, name, bread, age):
        self.name = name 
        self.bread = bread
        self.age = age
        
    def speak(self):
        pass
    
class Dog(Animals):
    def __init__(self, name, bread, age):
        super().__init__(name, bread, age)
        
    def speak(self):
        print(f"woof - {self.name} - {self.bread} - {self.age}")
        
class Cat(Animals):
    def __init__(self, name, bread, age):
        super().__init__(name, bread, age)
        
    def speak(self):
        print(f"Meow - {self.name} - {self.bread} - {self.age}")

class Cow(Animals):
    def __init__(self, name, bread, age, milk):
        super().__init__(name, bread, age)
        self.milk = milk
        
    def speak(self):
        print(f"moo - {self.name} - {self.bread} - {self.age} - {self.milk}")
        
dog = Dog("Ak-tosh", "Alabai", 2)
cat = Cat("Muska", "swinks", 1)
cow = Cow("Tamara", "Angust", 6, 'white')
dog.speak()
cat.speak()
cow.speak()




