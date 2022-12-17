from random import choices


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    def __bool__(self):
        return not self.__is_open
 
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if not (isinstance(value, int) and 0 <= value < 9):
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, value):
        self.__is_open = value


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N, self.M, self.total_mines = N, M, total_mines
        self.__pole_cells = self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines = choices(range(self.N * self.M), k=self.total_mines)
        N, M = self.N, self.M
        m = [[i * M + j in mines for j in range(M)] for i in range(N)]
        cells = [[None] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                cells[i][j] = c = Cell()
                if m[i][j]:
                    c.is_mine = True
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        if 0 <= i + p < N and 0 <= j + q < M and m[i + p][j + q]:
                            c.number += 1
                c.number -= int(c.is_mine)
        return cells

    def open_cell(self, i, j):
        if 0 <= i < self.N and 0 <= j < self.M:
            self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for i in range(self.N):
            for j in range(self.M):
                c = self.__pole_cells[i][j]
                if c.is_open:
                    print(' M ' if c.is_mine else f' {c.number} ',  end=' ')
                else:
                    print('[ ]', end=' ')
            print()


# Test:
pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
