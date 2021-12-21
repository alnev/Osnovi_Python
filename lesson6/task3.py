#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = str
    surname = str
    position = str
    _income = dict
class Position(Worker):
    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = str(name)
        self.surname = str(surname)
        self.position = str(position)
        self._income = {'wage': wage, 'bonus': bonus}
    def get_full_name (self):
        return self.name + ' ' + self.surname
    def get_total_income (self):
        return (self._income['wage']+ self._income['bonus'])

lead_employee = Position('Иван','Петров', 'Ведущий сотрудник' ,30000, 5000)
chief_employee = Position('Вера','Брежнева', 'Главный сотрудник',37000, 7000)
print (f"ФИО: {lead_employee.get_full_name()} Должность: {lead_employee.position} Месячный доход: {lead_employee.get_total_income()}")
print (f"ФИО: {chief_employee.get_full_name()} Должность: {chief_employee.position} Месячный доход: {chief_employee.get_total_income()}")


