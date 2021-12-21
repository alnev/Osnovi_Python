#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    real_number: float
    imaginary_number: float

    def __init__(self, real_number: float, imaginary_number: float):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def __add__(self, other: 'Complex'):
        return (Complex(self.real_number + other.real_number, self.imaginary_number + other.imaginary_number))

    def __mul__(self, other: 'Complex'):
        real1 = self.real_number * other.real_number
        real2 = self.imaginary_number * other.imaginary_number * -1
        img1 = self.real_number * other.imaginary_number
        img2 = self.imaginary_number * other.real_number
        real_number = real1 + real2
        imaginary_number = img1 + img2
        return (Complex(real_number, imaginary_number))

    def __str__(self):
        if self.imaginary_number > 0:
            complex = str('+')
        else:
            complex = str(' ')
        return (str(self.real_number) + complex + str(self.imaginary_number) + 'i')

a = Complex(10, 15)
b = Complex(5, 3)

print("Сложение :", a + b)
print("Умножение : ", a * b)
