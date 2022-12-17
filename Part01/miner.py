from random import choices


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]
        self.init()

    def init(self):
        randoms = sorted(choices(list(range(self.n ** 2)), k=self.m))
        for x in range(self.n):
            for y in range(self.n):
                if x * 10 + y in randoms:
                    setattr(self.pole[x][y], 'mine', True)
        for x in range(self.n):
            for y in range(self.n):
                self.pole[x][y].around_mines = self.get_around_miles(x, y)

    def show(self):
        for x in range(0, self.n):
            print(*[self.get_around_miles(x, y) if self.pole[x][y].fl_open else '#' for y in range(0, self.n)])

    def get_around_miles(self, i, j):
        number = 0
        for k in range(-1, 2):
            for m in range(-1, 2):
                ii, jj = k + i, m + j
                # print(f"Checking if the cell is in the pole: {ii, jj}")
                if ii < 0 or jj < 0 or ii >= self.n or jj >= self.n:
                    # print(f"Checking cell at: {ii, jj}")
                    continue
                if self.pole[ii][jj].mine:
                    number += 1
        return number


pole_game = GamePole(10, 12)

# Test:
assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')
N = 10
M = 10


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n

for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            # print(f"Correct: {get_around_mines(i,j)}")
            # print(f"Actual {i}, {j}: {pole_game.pole[i][j].around_mines}")
            actual = pole_game.pole[i][j].around_mines
            expected = get_around_mines(i,j)
            assert actual == expected, f"неверное число мин {actual} вокруг клетки с индексами {i, j}" \
                                                    f"correct is {expected}"
