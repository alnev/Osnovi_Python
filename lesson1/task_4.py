#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numb = input("Введи целое положительное число: ")
max_n = 0
chet = 0
while chet < len(numb):
    tek_n=int(numb[chet])
    if tek_n > max_n:
        max_n = tek_n
    chet = chet + 1
print("Максимальная цифра в числе:", max_n)

