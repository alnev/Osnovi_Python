#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

i = input("Введите Ваше число: ")
i2 = i+i
i3 = i+i+i
print("Итого: ",int(i)+int(i2)+int(i3))
