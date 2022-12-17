class ItemAttrs:
    def __getitem__(self, item):
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Test 1:
pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
print(pt.x, pt.y)
print(len(pt.__dict__))
