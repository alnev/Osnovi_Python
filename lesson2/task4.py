#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

stroka = input("Введите строку из нескольких слов с пробелами: ")
stroka = stroka.split()
for i, slovo in enumerate(stroka,1):
    print(i, slovo[:10])