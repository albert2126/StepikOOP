import time


class Mechanical:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Aragon:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Calcium:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slots = [None, None, None]

    def add_filter(self, slot_num, filter):
        if isinstance(filter, (Mechanical, Aragon, Calcium)[slot_num - 1]) and not self.slots[slot_num - 1]:
            self.slots[slot_num - 1] = filter

    def remove_filter(self, slot_num):
        if slot_num < 4:
            self.slots[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.slots)

    def water_on(self):
        return all(self.slots) and all([time.time() - f.date <= self.MAX_DATE_FILTER for f in self.slots])


# Test 1:
fff = Mechanical(time.time())
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
print(w)
print(*[my_water.slots])
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
