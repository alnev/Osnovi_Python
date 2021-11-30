#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

spisok = input("Введите элементы списка через пробелы: ")
spisok = spisok.split()

itogo =[]
for element in spisok[::2]:
    i = spisok.index(element)
    if i+1==len(spisok):
        itogo.append(element)
    else:
        itogo.extend([spisok[i+1],spisok[i]])
print(itogo)

