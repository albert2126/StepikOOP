class Digit:
    def __init__(self, value, cls=(int, float, complex)):
        self._check(value, cls)
        self.value = value

    @staticmethod
    def _check(val, cls):
        if type(val) not in cls:
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value, (int,))


class Float(Digit):
    def __init__(self, value):
        super().__init__(value, (float,))


class Positive(Digit):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def _check(val, cls):
        if type(val) not in cls or val <= 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def _check(val, cls):
        if type(val) not in cls or val >= 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


digits = [PrimeNumber(1),
          PrimeNumber(2),
          PrimeNumber(3),
          FloatPositive(1.0),
          FloatPositive(2.0),
          FloatPositive(3.0),
          FloatPositive(4.0),
          FloatPositive(5.0),
          ]
lst_positive = list(filter(lambda n: isinstance(n, Positive), digits))
lst_float = list(filter(lambda n: isinstance(n, Float), digits))


# Test:
print(*lst_positive, sep='\n')
print(*lst_float, sep='\n')

n = PrimeNumber(-1)  # Exception
