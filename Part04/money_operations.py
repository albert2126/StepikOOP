class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)
        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)
        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return self.__class__(self.money - other.money)


class Money:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('сумма должна быть числом')
        self._money = value

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value):
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


# Test 1:
m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError
