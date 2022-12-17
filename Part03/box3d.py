class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __oper(self, other, op, right=False):
        a, b = self, other
        if right:
            b, a = self, other
        return Box3D(eval(f"{a.width} {op} {b.width}"),
                     eval(f"{a.height} {op} {b.height}"),
                     eval(f"{a.depth} {op} {b.depth}")
                     )

    def __add__(self, other):
        return self.__oper(other, '+')

    def __sub__(self, other):
        return self.__oper(other, '-')

    def __mul__(self, other):
        return self.__oper(Box3D(other, other, other), '*')

    def __rmul__(self, other):
        return self.__oper(Box3D(other, other, other), '*', True)

    def __floordiv__(self, other):
        return self.__oper(Box3D(other, other, other), '//')

    def __mod__(self, other):
        return self.__oper(Box3D(other, other, other), '%')


# Test:
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box.width, box.height, box.depth)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box.width, box.height, box.depth)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
print(box.width, box.height, box.depth)
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box.width, box.height, box.depth)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
print(box.width, box.height, box.depth)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box.width, box.height, box.depth)
