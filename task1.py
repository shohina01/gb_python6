import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'red':
            print('Light is Red')
            time.sleep(7)
            print('Light is Yellow')
            time.sleep(2)
            print('Light is Green')
        elif self.__color == 'yellow':
            print('Light is Yellow')
            time.sleep(2)
            print('Light is Green')
            time.sleep(8)
            print('Light is Red')
        else:
            print('Light is Green')
            time.sleep(8)
            print('Light is Red')
            time.sleep(7)
            print('Light is Yellow')


instant = TrafficLight('green')
instant.running()

instant_2 = TrafficLight('red')
instant_2.running()

instant_3 = TrafficLight('yellow')
instant_3.running()
