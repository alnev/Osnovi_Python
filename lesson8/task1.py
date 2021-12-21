#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    date = str()
    def __init__(self, data):
        date = data

    @classmethod
    def data_to_number(cls, data):
        day = int(data[0: 2])
        month = int(data[3: 5])
        year = int(data[6: 10])
        print (cls, day, type(day), month, type(month) , year, type (year))

    @staticmethod
    def data_validation (data):
        k = True
        if int(data[0: 2]) > 31:
            print (f"Неверный день {data[0: 2]}")
            k = False
        if int(data[3: 5]) > 12:
            print (f"Неверный номер месяца {data[3: 5]}")
            k = False
        if int (data[6: 10]) < 1900 or len(data[6:]) !=4:
            print (f"Неверный номер года {data[6:]}")
            k = False
        if k==True:
            print (f"Введенная дата корректна {data}")

Data.data_to_number('18-12-2021')
Data.data_validation('18-12-2021')
Data.data_validation('48-15-20213')
