#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в
# формате чч:мм:сс. Используйте форматирование строк.

sec = int(input("Введите время в секундах: "))
hour = sec // 3600
min = sec % 3600 // 60
ss = sec % 3600 % 60
print(f"{hour:02d}:{min:02d}:{ss:02d}")