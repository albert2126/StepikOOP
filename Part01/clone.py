class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj = super().__new__(Point, self.x, self.y)
        obj.__init__(self.x, self.y)
        return obj

# Test:
p1 = Point(1, 2)
p2 = p1.clone()
print(type(p1), id(p1), p1.__dict__)
print(type(p2), id(p2), p2.__dict__)
