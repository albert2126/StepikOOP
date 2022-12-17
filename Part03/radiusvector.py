from math import sqrt


class RadiusVector:
    def __init__(self, *coords):
        if len(coords) == 1:
            self.__coords = [0] * coords[0]
        else:
            self.__coords = list(coords)

    def set_coords(self, *args):
        for i in range(min(len(self.__coords), len(args))):
            self.__coords[i] = args[i]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sqrt(sum((coord * coord for coord in self.__coords)))


# Test:
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.get_coords())
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_len, res_abs)
a, b, c = vector3D.get_coords()
print(a, b, c)
