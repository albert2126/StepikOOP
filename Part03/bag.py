class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []
        self.weight = 0

    def __check(self, index):
        if not (isinstance(index, int) and 0 <= index < len(self.things)):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        if self.weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things.append(thing)
        self.weight += thing.weight

    def __getitem__(self, item):
        self.__check(item)
        return self.things[item]

    def __setitem__(self, item, thing):
        self.__check(item)
        print(f"{self.weight} - {self.things[item].weight} + {thing.weight} > {self.max_weight}")
        if self.weight - self.things[item].weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things[item] = thing
        self.weight += self.things[item].weight + thing.weight

    def __delitem__(self, item):
        self.__check(item)
        del self.things[item]


# Test 1:
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# # bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError

# Test 2:
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания " \
                     "с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
