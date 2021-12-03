#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.
def summ (x, y, z):
    spisok= [x, y, z]
    spisok.sort()
#    print (spisok)
    return sum(spisok[1:])

print(summ(50, 15, 20))
print(summ(5, 8, 7))

