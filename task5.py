class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} is drawing with pen')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} is drawing with pencil')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} is drawing with handle')


f_inst = Pen('kitty')
f_inst.draw()

s_inst = Pencil('dog')
s_inst.draw()

t_inst = Handle('mouse')
t_inst.draw()
