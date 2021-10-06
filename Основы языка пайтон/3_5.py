from random import choice

def get_jokes(count, repeat = True):
    """" Функция по созданию шуток

    : param count: Количество шуток
    :return: None
    :repeat: Разрешение повторений слов
    """
    new_joke = []
    if repeat == True:
        for i in range(count):
            new_joke=[]
            new_joke.append(choice(nouns))
            new_joke.append(choice(adverbs))
            new_joke.append(choice(adjectives))
            print(*new_joke, end=', ')
    else:
        for i in range(count):
            new_joke = []
            new_joke.append(choice(nouns))
            nouns.remove(new_joke[0])
            new_joke.append(choice(adverbs))
            adverbs.remove(new_joke[1])
            new_joke.append(choice(adjectives))
            adjectives.remove(new_joke[2])
            print(*new_joke, end=', ')



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(5, repeat= False)