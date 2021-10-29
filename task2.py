class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, m_asp, thickness):
        m = (self._length * self._width * m_asp * thickness) / 1000
        return m


dushanbe = Road(20, 5000)
print(dushanbe.mass_of_asphalt(25,5))
