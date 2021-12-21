#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

#создаем файл со случайными числами
from random import randint
llist=''
for i in range (10):
    llist = llist + str(randint(0,20))+' '
with open("file_t5", "w") as file5:
    print (f"Сохраняем строку чисел в файл: {llist}")
    print(f'{llist}', file=file5)

#считаем сумму
with open("file_t5") as file:
    line = file.read().rstrip().split()
    print("Считали строку: ", line)
    sum =0
    for i, item in enumerate(line):
        sum=sum+int(line[i])
    print(f"сумма всех чисел: {sum}")
