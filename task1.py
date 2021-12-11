#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def delenie (x, y):
    try:
        return x/y
    except:
        return "Вы указали неверные данные."

print(delenie(4, 0))
print(delenie(6, 5))
print(delenie('d', 4))
print(delenie(77, 22))

sp1=int(input("Введите 1 число: "))
sp2=int(input("Введите 2 число: "))
print(delenie(sp1,sp2))







