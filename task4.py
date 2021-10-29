class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('is going')

    def stop(self):
        print('stopped')

    def turn(self, direction):
        print(f'turned to the {direction}')

    def show_speed(self):
        print(f'Your speed is: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('You were speeding!')
        else:
            print(f'Your speed is: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('You were speeding!')
        else:
            print(f'Your speed is: {self.speed}')


class PoliceCar(Car):
    pass


first = TownCar(40, 'blue', 'bmw', False)
first.go()
first.show_speed()
first.turn('left')

second = PoliceCar(120, 'black', 'hammer', True)
second.stop()
second.show_speed()
second.turn('right')

