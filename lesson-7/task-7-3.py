class Kletka:
    def __init__(self, cell):
        self._cell = cell

    def __str__(self):
        return str(self._cell)

    def __add__(self, other):
        return Kletka(self._cell + other._cell)

    def __sub__(self, other):
        if self._cell > other._cell:
            return Kletka(self._cell - other._cell)
        else:
            print("Ошибка, количество ячеек в основной клетке меньше вспомогательной!")

    def __mul__(self, other):
        return Kletka(self._cell * other._cell)

    def __truediv__(self, other):
        return Kletka(int(self._cell / other._cell))

    def make_order(self, count_in_row):
        last_cell = self._cell
        res = ""
        for rows in range(0, last_cell//count_in_row+1):
            if last_cell >= count_in_row:
                res = res + "*" * count_in_row + "\n"
                last_cell -= count_in_row
            else:
                res = res + "*" * last_cell + "\n"
        print(res)


k1 = Kletka(3)
k2 = Kletka(5)
k3 = Kletka(12)
k4 = Kletka(2)
k=(k1+k2+k3)/k4*k1-k3
print(k)
k.make_order(5)