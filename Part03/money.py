class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def convert(cls, money):
        if not money.cb:
            raise ValueError("Неизвестен курс валют.")
        return round(money.volume * cls.rates['rub'] / cls.rates[money.name], 1)

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyD:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume
        self.name = 'dollar'

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) == other.cb.convert(other)

    def __lt__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) < other.cb.convert(other)

    def __le__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) <= other.cb.convert(other)


class MoneyE:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume
        self.name = 'euro'

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) == other.cb.convert(other)

    def __lt__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) < other.cb.convert(other)

    def __le__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) <= other.cb.convert(other)


class MoneyR:
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume
        self.name = 'rub'

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __eq__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) == other.cb.convert(other)

    def __lt__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) < other.cb.convert(other)

    def __le__(self, other):
        if not self.cb or not other.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self) <= other.cb.convert(other)


# Test:
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
