class StringDigit(str):
    def __new__(cls, data):
        cls._check(data)
        return super().__new__(cls, data)

    def __add__(self, other):
        self._check(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit((other).__add__(self))

    @staticmethod
    def _check(string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")


# # Test 1:
# sd = StringDigit("123")
# print(sd)       # 123
# sd = sd + "456"  # StringDigit: 123456
# sd = "789" + sd  # StringDigit: 789123456
# sd = sd + "12f"  # ValueError

# Test 2:
sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
