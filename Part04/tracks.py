from collections import deque


class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *coords):
        if isinstance(coords[0], (int, float)) and isinstance(coords[1], (int, float)):
            self.__points = deque([PointTrack(coords[0], coords[1])])
        else:
            self.__points = deque(coords)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.appendleft(pt)

    def pop_back(self):
        return self.__points.pop()

    def pop_front(self):
        return self.__points.popleft()
    
    @property
    def points(self):
        return tuple(self.__points)


# Test:
tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
print(tr.points)
