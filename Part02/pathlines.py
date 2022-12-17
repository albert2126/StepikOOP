from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        return self.lines

    def get_length(self):
        ls = self.lines
        s = sum(sqrt((ls[i + 1].x - ls[i].x) ** 2 + (ls[i + 1].y - ls[i].y) ** 2) for i in range(len(ls) - 1))
        return s + sqrt(ls[0].x ** 2 + ls[0].y ** 2)

    def add_line(self, line):
        self.lines.append(line)


# Test:
p = PathLines(LineTo(10, 20), LineTo(10, 30))
print(p.get_length())
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
