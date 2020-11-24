from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ""
        for i in self.matrix:
            res = res + "\t".join(map(str, i)) + "\n"
        return res

    def get_element(self, i, j):
        return self.matrix[i - 1][j - 1]

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(0, len(self.matrix[0]))]
                       for i in range(0, len(self.matrix))])


def generate_matrix(i, j):
    return [[randint(1, 11) for _ in range(j)] for _ in range(i)]


m1 = generate_matrix(2, 3)
m2 = generate_matrix(2, 3)
matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
