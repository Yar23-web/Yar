from inspect import stack


class Person:
    def __init__(self, name, рівень):  
        self.name = name  
        self.рівень = рівень

    def атака(self):
        return f"{self.name} атакує!"

    def __str__(self):
        return f"{self.name} - Рівень: {self.рівень}"

class Воїн(Person):
    def атака(self):
        return f"{self.name} атакує мечем!"

class Маг(Person):
    def атака(self):
        return f"{self.name} атакує заклинанням!"

class Лучник(Person):
    def атака(self):
        return f"{self.name} стріляє з лука!"

def demonstrate(person):"person"()

person = [
    Воїн("Артур", 7),
    Маг("Мерлін", 7),
    Лучник("Робін", 7)
]

for персонаж in person:
    demonstrate(person)
