class Stationery:
    def __init__(self, name):
        self.title = name
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка. {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка. {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка. {self.title}')

s = Stationery('Канц')
p = Pen('Ручка')
pc = Pencil('Карандаш')
h = Handle('Маркер')

s.draw()
p.draw()
pc.draw()
h.draw()