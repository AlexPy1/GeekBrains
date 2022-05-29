class Car:
    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        print(f'{self.name} поехала. Скорость {self.speed}')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self,direction):
        print(f'{self.name} повернула {direction} ')

    def show_speed(self):
        print(self.name, self.speed)



class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} Превышение скорости. Скорость {self.speed}')
        else:
            print(self.name, self.speed)
        if self.is_police == True:
            print(f'Остановите машину {self.name}!')


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} Превышение скорости. Скорость {self.speed}')
        else:
            print(self.name, self.speed)

class PoliceCar(Car):
    pass

t = TownCar(59,'blue','Nissan', False)
s = SportCar(100, 'red', 'Audi', True)
w = WorkCar(50, 'white', 'Lada', False)
p = PoliceCar(80, 'black', 'Police-BMW', False)

t.turn("Налево")
s.go()
w.go()
p.go()
print()
t.show_speed()
s.show_speed()
w.show_speed()
p.stop()