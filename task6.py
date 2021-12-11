#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

#вариант 1
def slovo (word):
    return word.capitalize()

#вариант 2
def slovo2 (word):
    sl=word[0]
    sl=sl.upper()
    sl=sl+word[1:]
    return sl


#stroka = input("Введите строку: ")
stroka = 'идем гулять на улицу Парковая'
stroka1 = []
stroka2 = []
slova_str = stroka.split()
print(stroka , slova_str )
for i in slova_str:
    stroka1.append(slovo(i))
    stroka2.append(slovo2(i))

print(" ".join(stroka1))
print(" ".join(stroka2))
