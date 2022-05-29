class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell
    def __sub__(self, other):
        if self.cell >= other.cell:
            return self.cell - other.cell
        else:
            return (f'Оперция невозможна.{self.cell}<{other.cell}')
    def __mul__(self, other):
        return self.cell * other.cell
    def __truediv__(self, other):
        return self.cell // other.cell
    def __floordiv__(self, other):
        return int(self.cell / other.cell)


    def make_oder(self, row):
        count = 0
        str = ''
        for i in range(self.cell):
            if count<row:
                str+='*'
                count+=1
            else:
                str+='\n*'
                count=1

        return str





cell_1 = Cell(13)
cell_2 = Cell(12)
print(cell_1+cell_2)
print(cell_1 - cell_2)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_1//cell_2)
print(cell_2.make_oder(6))


