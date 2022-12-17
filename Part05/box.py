from copy import deepcopy


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._weight = 0

    def add_thing(self, obj):
        if obj[1] + self._weight > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._weight += obj[1]


class BoxDefender:
    def __init__(self, box):
        self._box = box

    def __enter__(self):
        self._temp = deepcopy(self._box)
        return self._temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self._box._things[:] = self._temp._things
            self._box._weight = self._temp._weight
        return False


# Test:
box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))

print(box._things)
