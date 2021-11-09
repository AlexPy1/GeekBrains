class Sklad:
    def __init__(self,name, tp, count,spot = 0, podraz = 'склад', my_sklad = {}):
        self.name = name
        self.tp = tp
        self.count = count
        self.spot = spot
        self.podraz = podraz
        self.my_sklad = my_sklad

    @property
    def ssave(self):
        try:
            self.my_sklad.setdefault(self.name,[self.spot,self.tp,self.count, self.podraz])
            return self.my_sklad
        except Exception:
            print("Ошибка")

    def peredacha(self, name, new_pod, kol):
        try:

            if name in self.my_sklad:
                new_name = new_pod + '_' + str(name)

                if kol < self.count:
                    self.my_sklad[name][2] = self.count - kol
                    self.my_sklad.setdefault(new_name, [new_pod, self.tp, kol])
                elif kol == self.count:
                    self.my_sklad[name][2] = 0
                    self.my_sklad.setdefault(new_name, [new_pod, self.tp, kol])
                elif kol > self.count:
                    raise ValueError('Слишком большое количество')
            else:
                raise ValueError('Такого товара нет!')
        except ValueError as err:
            print(err)

            return self.my_sklad
        except Exception:
            print('Ошибка')

    def util(self, name, kol):
        if name in self.my_sklad:
            self.my_sklad[name][2] -= kol
            if kol > self.my_sklad[name][2]:
                return 'Слишком большое количество!'

        return self.my_sklad

    def info(self):
        print(self.my_sklad)


class OrgTeh:
    def info(self):
        pass

class Prin(OrgTeh):

    def pechat(self, text):
        print(text)




class Kser(OrgTeh):

    def coppy(self,text):
        my_copy = []
        my_copy.append(text)
        return my_copy




class Scaner(OrgTeh):

    def scn(self):
        q = ''
        res = []
        while True:
            q = input('Я сканер. Добавляю строки в список. Для выхода введите q: ')
            if q == 'q':
                break
            else:
               res.append(q)
        return res




def upr():
    while True:
        print('Что Вы хотите сделать?\nВоспользоваться оргтехникой введите 1.\nВоспользоваться складом введите 2.\nДля выхода введите 0.')
        inp = int(input())
        if inp == 1:
            print('Чтобы воспользоваться принтером введите 1.\nЧтобы воспользоваться сканером введите 2.\nЧтобы воспользоваться ксероксом введите 3.\nДля выхода введите 0')
            inp = int(input())
            if inp == 1:
                p = Prin()

                p.pechat(input('Введите текст, для печати'))
            elif inp == 2:
                s = Scaner()

                print(s.scn())
            elif inp == 3:
                k = Kser()

                print(k.coppy(input('Введите текст для копирования')))
            elif inp == 0:
                break
            else:
                print('Неверный ввод!')
        elif inp == 0:
            break
        elif inp == 2:
            print('Введите 1 для информации о складе.\nВведите 2 для отправки на склад товара.\nВведите 3 для передачи товара со склада.\nВведите 4  для утилизации товара.\nВведите 0 для выхода. ')
            inp = int(input())
            if inp == 0:
                break
            elif inp == 2:
                global upra
                try:
                    upra = Sklad(input('Введите название'), input('Введите тип'), int(input('Введите количество')))
                    upra.ssave
                    print('Товар отправлен на склад')
                except Exception:
                    print('Ошибка')
            elif inp == 1:
                try:
                    upra.info()
                except Exception:
                    print('Ошибка')
            elif inp == 3:
                try:
                    upra.peredacha(input('Введите имя'),input('Введите подразделение'), int(input('Введите количество')))
                except Exception:
                    print('Ошибка')
            elif inp == 4:
                try:
                    print(upra.util(input('Введите имя'), int(input('Введите количество'))))
                except Exception:
                    print('Ошибка')

        else:
            print("Неверный ввод")

upr()