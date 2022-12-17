class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things=None):
        if things is not None and not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        if things is not None:
            for key in things:
                self._check_key(key)
            super().__init__(things)
        else:
            super().__init__()

    def _check_key(self, key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __setitem__(self, key, value):
        self._check_key(key)
        super().__setitem__(key, value)


# Test:
th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError
