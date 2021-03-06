#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def stepen (x: int, y: int) -> float:
    itog = 1
    for i in range(abs(y)):
        itog = itog* x
    if y >= 0:
        return itog
    else:
        return 1/itog

print(stepen(4,3))
print(stepen(4,-3))
print(stepen(4,0))
print(stepen(4,1))
