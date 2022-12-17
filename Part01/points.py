class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(a, a) for a in range(1, 2000, 2)]
setattr(points[1], 'color', 'yellow')

print(len(points))
