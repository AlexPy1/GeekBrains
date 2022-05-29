class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        f_n = f'{self.name} {self.surname}'
        return f_n

    def get_total_income(self):

        sum = self._income['wage'] + self._income['bonus']
        return sum

a = Position('Alex', 'Py', 'Py_dev', 150_000, 5000)
b = Position('Andrey', 'Ja', 'Ja_dev', 100_000, 10000)
print(a.get_full_name())
print(a.get_total_income())
print(b.get_full_name())
print(b.get_total_income())