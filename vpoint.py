import random
import math

class VPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return VPoint(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar):
        return VPoint(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    @staticmethod
    def random():
        angle = random.uniform(0, 2 * math.pi)
        return VPoint(math.cos(angle), math.sin(angle))

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
