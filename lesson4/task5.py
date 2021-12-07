#5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

#пример последовательности для 2 чисел
print([x for x in range(100, 103) if x%2==0])
from functools import reduce
items = [x for x in range(100, 103) if x%2==0]
all = reduce(lambda x, y: x * y, items)
print(all)

#по задаче  слишком большое число выходит
from functools import reduce
items = [x for x in range(100, 1001) if x%2==0]
all = reduce(lambda x, y: x * y, items)
print(all)
