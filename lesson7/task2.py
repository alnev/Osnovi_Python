#2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
class Сlothes (ABC):
    name = str
    def __init__(self, name):
        self.name = str(name)
    @property
    @abstractmethod
    def fabric_consumption (self):
        pass
class Coat(Сlothes):
    size: float
    def __init__(self, name,V):
        super(Coat, self).__init__(name)
        self.size = float(V)
    @property
    def fabric_consumption(self):
        return round((self.size / 6.5 + 0.5),2)

class Suit(Сlothes):
    height: float
    def __init__(self, name, H):
        super(Suit, self).__init__(name)
        self.height = float(H)
    @property
    def fabric_consumption(self):
        return round((2 * self.height + 0.3),2)

coat = Coat("Пальто", 25)
suit = Suit("Костюм", 1.8)
print (f"Расход ткани на {coat.name} будет {[coat.fabric_consumption]} м2")
print (f"Расход ткани на {suit.name} будет {[suit.fabric_consumption]} м2")
