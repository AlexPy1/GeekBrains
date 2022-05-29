# date = 12-10-2005
class MyErr(Exception):
    def __init__(self, text):
        self.text = text


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def for_int(cls,date):
        try:
            date = date.split('-')
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])

        except (ValueError,AttributeError) as err:
            print(err)
        else:
            return cls(day, month, year)


    @staticmethod
    def valid(obj):
        new_date=[]
        try:
            if 0 < obj.day <= 31:
                new_date.append(obj.day)
            else:
                raise MyErr('Некорректный день!')
            if 0< obj.month < 13:
                new_date.append(obj.month)
            else:
                raise MyErr('Некорректный месяц!')
            if 0 < obj.year < 3500:
                new_date.append(obj.year)
            else:
                raise MyErr('Некорректный год!')
        except (MyErr, AttributeError) as err:
            new_date=[]
            print(err)
        return new_date




a = Date.for_int('12-13-2014')

print(Date.valid(a))



