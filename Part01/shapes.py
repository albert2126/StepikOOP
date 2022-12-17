from random import choice


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Ellipse:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


shapes = [choice((Line, Rect, Ellipse))(*(choice(range(10)) for _ in range(4))) for _ in range(217)]

for shape in shapes:
    if isinstance(shape, Line):
        shape.sp = shape.ep = (0, 0)


# Tests:
print(len(shapes))
# for sh in shapes:
#     print(type(sh), sh.sp, sh.ep)
