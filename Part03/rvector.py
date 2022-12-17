class RadiusVector:
    def __init__(self, *coords):
        self.coords = list(coords)

    def __getitem__(self, item):
        return self.coords[item] if isinstance(item, int) else tuple(self.coords[item])

    def __setitem__(self, item, value):
        self.coords[item] = value


# Test:
v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
