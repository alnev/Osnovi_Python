#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#Выполните вызов методов и также покажите результат.

class Car:
    speed = float
    color = str
    name = str
    police = bool
    def __init__(self, speed, color, name, police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
    def go (self):
        print (f"Машина {self.name} поехала")
    def stop (self):
        print (f"Машина {self.name} остановилась")
    def turn (self, direction):
        if direction == 'right':
            print(f"Машина {self.name} поворачивает направо")
        elif direction == 'left':
            print(f"Машина {self.name} поворачивает налево")
        else:
            print(f"Машина {self.name} едет прямо")
    def show_speed (self):
        print (f"Машина {self.name} едет со скоростью {self.speed}")
    def check_police (self):
        if self.police == 1:
            print (f"Машина {self.name} принадлежит полиции")
        else:
            print (f"Машина {self.name} не принадлежит полиции")
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превышает допустимую скорость в 60 км/ч")
        else:
            print (f"Машина {self.name} едет с допустимой скоростью")
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превышает допустимую скорость в 40 км/ч")
        else:
            print(f"Машина {self.name} едет с с допустимой скоростью")
class PoliceCar(Car):
    police = True

ford = PoliceCar(100, 'White', 'Town Police')
tatra = WorkCar(50, 'Black', 'Truck')
mazda = TownCar(60, 'Yellow', 'Taxi')
toyota = SportCar(120, 'Red', 'Racer')

mazda.show_speed()
mazda.go()
mazda.check_police()

tatra.show_speed()

ford.check_police()

toyota.go()
toyota.turn('left')
