from operator import add, sub


class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __valid(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self.__valid(other)
        return Vector(*(map(add, self.coords, other.coords)))

    def __sub__(self, other):
        self.__valid(other)
        return Vector(*(map(sub, self.coords, other.coords)))

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *coords):
        if len(tuple(filter(lambda x: isinstance(x, int), coords))) != len(coords):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*coords)

    # def __add__(self, other):
    #     _class = Vector if not isinstance(other, type(self)) else type(self)
    #     return _class(*tuple(map(add, self.coords, other.coords)))

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return super().__add__(other)
        return __class__(*tuple(map(add, self.coords, other.coords)))

    # def __sub__(self, other):
    #     _class = Vector if not isinstance(other, type(self)) else type(self)
    #     return _class(*tuple(map(add, self.coords, other.coords)))

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            return super().__add__(other)
        return __class__(*tuple(map(add, self.coords, other.coords)))


# Test:
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
# print((v1 + v2).get_coords())
assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
