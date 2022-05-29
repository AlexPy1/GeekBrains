import time


class TrafficLight:
    __color = ['красный','желтый','зеленый', 'желтый']

    def running(self):
        s = 0

        while s < 10:
            for i in self.__color:
                print(i)
                if i == 'красный':
                    time.sleep(7)
                    s+=1
                elif i == 'желтый':
                    time.sleep(2)
                    s+=1
                else:
                    time.sleep(3)
                    s+=1

a = TrafficLight()
print(a.running())