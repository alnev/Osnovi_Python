#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("file_t3", "r") as file:
    summa =0
    lines = file.readlines()
    for stroka in lines:
        name, salary = stroka.split()
        if int(salary) < 20000:
            print (f"Оклад сотрудника {name} менее 20 тысяч и равен: ", salary)
        summa=summa + int(salary)
    print("Средняя зарплата сотрудников: ", summa/len(lines))
