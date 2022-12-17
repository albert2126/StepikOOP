from operator import add, sub, mul


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __validate(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return True

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*map(lambda x: x + other, self.coords))
        if self.__validate(other):
            return Vector(*map(add, self.coords, other.coords))

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            for i in range(len(self.coords)):
                self.coords[i] += other
        elif self.__validate(other):
            for i in range(len(self.coords)):
                self.coords[i] += other.coords[i]
        return self

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*map(lambda x: x - other, self.coords))
        if self.__validate(other):
            return Vector(*map(sub, self.coords, other.coords))

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            for i in range(len(self.coords)):
                self.coords[i] -= other
        elif self.__validate(other):
            for i in range(len(self.coords)):
                self.coords[i] -= other.coords[i]
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*map(lambda x: x * other, self.coords))
        if self.__validate(other):
            return Vector(*map(mul, self.coords, other.coords))

    def __eq__(self, other):
        return all(map(lambda x, y: x == y, self.coords, other.coords))
