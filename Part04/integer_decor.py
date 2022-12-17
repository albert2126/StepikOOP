def integer_params_decorated(func):
    def wrapper(*args, **kwargs):
        print(*args)
        if not all(map(lambda x: type(x) == int, list(args[1:]) + list(kwargs.values()))):
            raise TypeError("аргументы должны быть целыми числами")
        return func(*args, **kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


# Test:
v = Vector(10, 20, 30)
print(*v)
assert v[0] == 10 and v[1] == 20 and v[2] == 30, "неверные значения координат вектора, взятые по индексам"
# v1 = Vector(1.1, 20, 30)
v.set_coords(1, 2, reverse=True)
