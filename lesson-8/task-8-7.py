# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        b = f"+{self.b}i" if self.b > 0 else f"{self.b}i"
        return f"{self.a}" + b

    def __mul__(self, other):
        # z = z1⋅z2 = (a1a2−b1b2) + (a1b2 + b1a2)i
        return Complex(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)

    def __add__(self, other):
        # z = (a1 + a2) + (b1 + b2)i
        return Complex(self.a + other.a, self.b + other.b)


# z1=5−6i + z2=−3+2i = 2− 4i

z1 = Complex(5, -6)
z2 = Complex(-3, 2)

print(z1 + z2)

# z1=2+3i * z2=−1+i  = −5−i
z1 = Complex(2, 3)
z2 = Complex(-1, 1)
print(z1*z2)