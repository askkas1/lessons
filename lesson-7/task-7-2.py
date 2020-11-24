from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def rashod(self):
        pass

    def __add__(self, other):
        return self.rashod + other.rashod

class Palto(Clothes):
    def __init__(self, size):
        super().__init__()
        self._size = size

    @property
    def rashod(self):
        return round(self._size / 6.5 + 0.5, 3)


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self._height = height

    @property
    def rashod(self):
        return round(2 * self._height + 0.3, 3)


p = Palto(38)
print(p.rashod)

c = Costume(55)
print(c.rashod)

c2= Costume(59)
print(c2.rashod)

print(c.rashod+p.rashod+c2.rashod)