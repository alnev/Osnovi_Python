#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.

import json
result=[]
loss={}
profit={}
average_profit=[]
with open("file_t71", "r") as file1, open ("file_t72.json", "w") as file2 :
    for line in file1.readlines():
        name, pusto, prof, los = line.strip().split()
        proff = int(prof)- int(los)
        if proff >0:
            profit.update({name: proff})
            average_profit.append(proff)
        else:
            loss.update({name: proff})
    result.append(profit)
    result.append(loss)
    result.append({"average_profit": sum(average_profit)/len(average_profit)})
    json.dump(result,file2)
