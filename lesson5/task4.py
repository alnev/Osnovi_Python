#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}
with open ("file_t4_1", "r") as file41, open ("file_t4_2", "w") as file42:
    for stroka in file41.readlines():
#        print (stroka.strip().split(' - '))
        line, number = stroka.strip().split(' - ')
#        print (f"{dictionary[line]} - {number}\n")
        file42.write(f"{dictionary[line]} - {number}\n")
