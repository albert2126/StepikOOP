class PolyLine:
    def __init__(self, *coords):
        # self.start_coords = coords[0]
        self.coords = list(coords)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        del self.coords[indx]

    def get_coords(self):
        return self.coords

