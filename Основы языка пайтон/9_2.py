
class Road:

    def __init__(self,length, width):
        self._length = length
        self._width = width

    def sum_mass(self):

        sum = self._length * self._width * 25 * 5
        return sum//1000

a = Road(5000,20)
print(f'{a.sum_mass()} т')
