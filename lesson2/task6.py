"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

my_sklad = []
i = int(input("Введите количество записей о товарах: "))
j = 1
while j <= i:
    my_ed = dict({'название товара': input("Введите название товара: "),
                  'цена': input("Введите цену товара: "),
                  'количество': input("Введите количество товара: "),
                  'ед': input("Введите единицы товара: ")})
    my_sklad.append((j,my_ed))
    j = j + 1
print (my_sklad)

# пример готового списка
#my_sklad = [(1, {'название товара': 'молоко', 'цена': '50', 'количество': '10', 'ед': 'пакет'}),
#            (2, {'название товара': 'яблоко', 'цена': '90', 'количество': '20', 'ед': 'килограмм'}),
#            (3, {'название товара': 'дыня', 'цена': '70', 'количество': '20', 'ед': 'шт'})
#            ]
#print(my_sklad)


new_sklad = {}

for element in my_sklad:
    i, j = element
    for key, value in j.items():
        value_element = new_sklad.get(key,[])
        if value not in value_element:
            value_element.append(value)
        new_sklad[key] = value_element
print(new_sklad)