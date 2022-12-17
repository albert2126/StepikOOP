class Track:
    def __init__(self, start_x, start_y ):
        self.start_x = start_x
        self.start_y = start_y
        self.segment = []

    def __isvalid(self, index):
        if not (isinstance(index, int) and 0 <= index < len(self.segment)):
            raise IndexError('некорректный индекс')
        return True

    def add_point(self, x, y, speed):
        self.segment.append([(x, y), speed])

    def __getitem__(self, item):
        self.__isvalid(item)
        return self.segment[item]

    def __setitem__(self, item, value):
        self.__isvalid(item)
        self.segment[item][1] = value


# Test:
tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError
