from random import randint, choice


def to_ordinal(x, y, size):
    return x + size * y


def from_ordinal(n, size):
    return n % size, n // size


def tuple_to_set(tps, size):
    return set((to_ordinal(x, y, size) for x, y in tps))


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x, self._y = x, y
        self._is_move = True
        self._cells = [1] * length
        self._is_killed = False

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def get_cells_coords(self):
        if self._tp == 1:
            return tuple([(x, self._y) for x in range(self._x, self._x + self._length)])
        else:
            return tuple([(self._x, y) for y in range(self._y, self._y + self._length)])

    def __len__(self):
        return self._length

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def get_around(self, size):
        cells = self.get_cells_coords()
        xmin, xmax = max([0, min([c[0] for c in cells])]), min([size - 1, max([c[0] for c in cells])])
        ymin, ymax = max([0, min([c[1] for c in cells])]), min([size - 1, max([c[1] for c in cells])])
        return [(x, y) for x in range(xmin - 1, xmax + 2) for y in range(ymin - 1, ymax + 2) if x >= 0 and y >= 0]

    def is_collide(self, ship):
        cells = self.get_cells_coords()
        xmin, xmax = min([c[0] for c in cells]), max([c[0] for c in cells])
        ymin, ymax = min([c[1] for c in cells]), max([c[1] for c in cells])
        area = [(x, y) for x in range(xmin - 1, xmax + 2) for y in range(ymin - 1, ymax + 2) if x >= 0 and y >= 0]
        return bool(set(ship.get_cells_coords()) & set(area))

    def is_out_pole(self, size):
        return self._x < 0 or self._y < 0 or \
               self._tp == 1 and self._x + self._length >= size or \
               self._tp == 2 and self._y + self._length >= size

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, item, value):
        self._cells[item] = value
        if value == 2:
            self._is_move = False
        if all([c == 2 for c in self._cells]):
            self._is_killed = True


class GamePole:
    def __init__(self, size=10):
        self._size = size
        self._ships = []
        self._all_ships = []
        self._available = set(range(size * size))  # Free cells as a 1D list
        self._cells = [[0 for _ in range(self._size)] for _ in range(self._size)]

    def init(self):
        self._all_ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                           Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                           Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                           Ship(1, tp=randint(1, 2))]
        attempt = 0
        while attempt < 10:
            attempt += 1
            try:
                self._build()
            except (IndexError, RecursionError):
                tp = randint(1, 2)
                for ship in self._all_ships:
                    ship._tp = tp
            else:
                break

    def _build(self):
        for ship in self._all_ships:
            ordinal = choice(list(self._available))
            x, y = from_ordinal(ordinal, self._size)
            ship.set_start_coords(x, y)
            cells = tuple_to_set(ship.get_cells_coords(), self._size)
            trial = 0
            while ship.is_out_pole(self._size) or cells & self._available != cells:
                trial += 1
                ordinal = choice(list(self._available))
                x, y = from_ordinal(ordinal, self._size)
                ship.set_start_coords(x, y)
                cells = tuple_to_set(ship.get_cells_coords(), self._size)
                if trial >= 10:
                    raise RecursionError
            self._ships.append(ship)
            for x, y in ship.get_cells_coords():
                self._cells[y][x] = 1
            self._available = self._get_available()

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._all_ships:
            init_coords = ship.get_cells_coords()
            self._ships.remove(ship)
            ship.move(1)
            cells = tuple_to_set(ship.get_cells_coords(), self._size)
            self._available = self._get_available()
            if ship.is_out_pole(self._size) or cells & self._available != cells:
                ship.move(-1)
                ship.move(-1)
                cells = tuple_to_set(ship.get_cells_coords(), self._size)
                self._available = self._get_available()
                if ship.is_out_pole(self._size) or cells & self._available != cells:
                    ship.move(1)
            self._ships.append(ship)
            current_coords = ship.get_cells_coords()
            if init_coords != current_coords:
                for x, y in init_coords:
                    self._cells[y][x] = 0
                for x, y in current_coords:
                    self._cells[y][x] = 1
                self._available = self._get_available()

    def show(self):
        for y in range(self._size):
            for x in range(self._size):
                print('.' if self._cells[y][x] == 0 else 'O' if self._cells[y][x] == 1 else 'X', end=' ')
            print()

    def get_pole(self):
        return tuple(tuple(s) for s in self._cells)

    def _get_available(self):
        avail = set((range(self._size * self._size)))
        for ship in self._ships:
            avail -= tuple_to_set(ship.get_around(self._size), self._size)
        return avail


# Test 0:
# Test 1:
# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# pole.show()

# Test 2:
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта " \
                                                                              "класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
# assert s1.is_collide(
#     s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()

for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
# pole_size_8.show()
