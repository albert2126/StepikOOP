from random import randint


class Cell:
    def __init__(self):
        self.value = 0  # 1 - cross, 2 - zero

    def __bool__(self):
        return not bool(self.value)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.__N = 3
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(self.__N))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def __isvalid(self, coord):
        x, y = coord
        if not (isinstance(x, int) and isinstance(y, int) and 0 <= x < self.__N and 0 <= y < self.__N):
            raise IndexError('некорректно указанные индексы')

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(self.__N))

    def show(self):
        [print(*(self[x, y] for y in range(3)), sep=' ') for x in range(3)]
        print('-' * 5)

    def human_go(self):
        x, y = tuple(map(int, input('Enter space-separated coordinates, x y: ').split()))
        self[x, y] = self.HUMAN_X

    def computer_go(self):
        busy, x, y = True, -1, -1
        while busy:
            n = randint(0, 8)
            x, y = n // 3, n % 3
            busy = bool(self.pole[x][y])
        self[x, y] = self.COMPUTER_O

    def __getitem__(self, coord):
        self.__isvalid(coord)
        row, col = coord
        if isinstance(row, slice):
            return tuple(self.pole[x][col].value for x in range(self.__N))
        elif isinstance(col, slice):
            return tuple(self.pole[row][x].value for x in range(self.__N))
        else:
            return self.pole[row][col].value

    def __setitem__(self, coord, value):
        if self[coord]:
            raise ValueError('клетка уже занята')
        self.pole[coord[0]][coord[1]].value = value
        self.is_human_win = self.__win(self.HUMAN_X)
        self.is_computer_win = self.__win(self.COMPUTER_O)

    def __bool__(self):
        return any(map(lambda c: not c, [self[x, y] for x in range(3) for y in range(3)])) \
            and not any([self.is_human_win, self.is_human_win, self.is_draw])

    def __win(self, mark):
        def func(c):
            return c.value == mark

        return any([all(map(func, [self.pole[x][y] for y in range(3)])) for x in range(3)]) \
            or any([all(map(func, [self.pole[x][y] for x in range(3)])) for y in range(3)]) \
            or all(map(func, [self.pole[x][x] for x in range(3)])) \
            or all(map(func, [self.pole[x][2 - x] for x in range(3)]))

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value


# Test game 1:
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

# # Test game 2:
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")

# Test 2:
# g = TicTacToe()
# g.init()
# # print(g[0, 0])
# assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
# g[1, 1] = 1
# g[2, 1] = 2
# assert g[1, 1] == 1 and g[
#     2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно " \
#                 "работает считывание значений)"
#
# try:
#     res = g[3, 0]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
#
# try:
#     g[3, 0] = 5
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"
#
# g.init()
# g[0, 0] = 1
# g[1, 0] = 2
# g[2, 0] = 3
#
# # print(g[0, :])
# # print(g[1, :])
# # print(g[:, 0])
# assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), \
#     "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
#
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
# res = cell.is_free
# cell.is_free = True
# assert bool(cell), "функция bool вернула False для свободной клетки"
