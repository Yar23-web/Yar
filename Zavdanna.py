import math

class PlochaTrykutnyka:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  

    def is_valid(self):
        """Перевіряє, чи можна побудувати трикутник із заданими сторонами."""
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def area(self):
        """Обчислює площу трикутника за формулою Герона."""
        if not self.is_valid():
            return "Неможливо обчислити площу. Трикутник не існує."
        p = (self.a + self.b + self.c) / 2 
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

a = 3
b = 4
c = 5

triangle = PlochaTrykutnyka(a, b, c)

if triangle.is_valid():
    print(f"Площа трикутника: {triangle.area()}")
else:
    print("Трикутник із такими сторонами не існує.")
