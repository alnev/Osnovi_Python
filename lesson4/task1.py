#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

#взял из методички - немного добавил

from sys import argv
script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Параметр 1(продуктивность): ", first_param)
print("Параметр 2(ставка в час): ", second_param)
print("Параметр 3(премия): ", third_param)
print('Итого зарплата: ', int(first_param) * int(second_param) + int(third_param))



