#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

reyting = [9, 6, 6, 4, 3, 2, 2]
print(reyting)
new = int(input("Введите новый элемент рейтинга: "))

if new <= reyting[-1]:
    reyting.append(new)
else:
    i = 0
    while i < len(reyting):
        if new > reyting[i]:
            reyting.insert(i, new)
            break
        i = i+1
print(reyting)
