#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    m_view = []
    m_summa = []
    n = []
    def __init__(self, matrix_data: list):
        self.matrix_data = matrix_data
        self.rows = len(self.matrix_data)
        self.items = len(self.matrix_data[0])
        print ("Новый объект - матрица ")

    def __str__(self):
        self.m_view.clear()
        for element in self.matrix_data:
            self.m_view.append(element)
        return ('\n'.join(map(str, self.m_view)))

    def __add__(self, other):
        print ("Сумма матриц: ")
        for row in range(0, self.rows):
            self.n.clear()
            for idx in range(0, self.items):
                self.n.append((other.matrix_data[row])[idx] + (self.matrix_data[row])[idx])
            self.m_summa.append(str(self.n))
        return (self.m_summa)

matrix_a = Matrix([[1, 2, 3, 4, 5],[8, 1, 3, 5, 7],[5, 0, 9, 0, 8],])
print(matrix_a)
matrix_b = Matrix([[1, 1, 1, 1, 1],[2, 2, 2, 2, 2],[3, 3, 3, 3, 3],])
print(matrix_b)
matrix_c = Matrix(matrix_b + matrix_a)
print(matrix_c)
