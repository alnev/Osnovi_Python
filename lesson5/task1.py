#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("file_t1", "a") as file:
    stroka = input("Введите строку для файла: ")
    while stroka:
        file.write(stroka+'\n')
        stroka = input("Введите снова строку для файла: ")
