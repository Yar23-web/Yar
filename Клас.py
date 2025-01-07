import math

class Cylinder:
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height
    
    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height
    
cylinder = Cylinder(radius=5, height=10)
cylinder_volume = cylinder.volume()
print(cylinder_volume) 
