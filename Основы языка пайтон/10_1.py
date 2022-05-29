class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for i in self.matrix:
            for x in i:
                res += str(x) + '\t'
            res += '\n'
        return res

    def __add__(self, other):
        res = ''
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[0])):
                a_1 = self.matrix[i][n]
                a_2 = other.matrix[i][n]
                res += str(a_1+a_2) +'\t'
            res += '\n'
        return res


mat_1 = Matrix([[1,2,7],[3,4,6],[5,6,5]])
mat_2 = Matrix([[6,5,7],[4,3,6],[2,1,5]])
print(mat_1)
print(mat_2)

print(mat_1 + mat_2)