

class Palto:
    def __init__(self, size):
        self._size = size

    @property
    def get_rashod(self):
        return self._size / 6.5 + 0.5


class Costume:
    def __init__(self, height):
        self._height = height

    @property
    def get_rashod(self):
        return 2 * self._height + 0.3


class Clothes:
    _rashod = 0
    obj = []

    @property
    def get_rashod(self):
        return str(round(self._rashod,3))

    def add_Palto(self, size):
        p = Palto(size)
        self.obj.append(p)
        self._rashod +=  p.get_rashod

    def add_Costume(self, height):
        p = Costume(height)
        self.obj.append(p)
        self._rashod +=  p.get_rashod


cl = Clothes()
cl.add_Palto(15)
cl.add_Palto(10)
cl.add_Costume(15)
cl.add_Costume(55)


print(cl.get_rashod)
