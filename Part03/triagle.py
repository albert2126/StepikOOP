from math import sqrt


class TriangleSide:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not value > 0:
            raise ValueError('длины сторон треугольника должны быть положительными числами')
        setattr(instance, self.name, value)


class Triangle:
    a, b, c = TriangleSide(), TriangleSide(), TriangleSide()

    def __init__(self, a, b, c):
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError('с указанными длинами нельзя образовать треугольник')
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Test:
tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"

