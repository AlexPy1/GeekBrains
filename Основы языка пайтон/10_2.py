from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v=0, h=0):
        self.v = v # размер(пальто)
        self.h = h # рост (костюм)

    @abstractmethod
    def sum_mat(self):
       pass

class Coat(Clothes):
    @property
    def sum_mat(self):
        sum_p = (self.v/6.5+0.5)
        return sum_p

class Suit(Clothes):
    @property
    def sum_mat(self):
        sum_c = (self.h*2+0.3)
        return sum_c

c = Coat(v= 48)
s = Suit(h = 180)
res = c.sum_mat+s.sum_mat

print(c.sum_mat)
print(s.sum_mat)
print(res)
