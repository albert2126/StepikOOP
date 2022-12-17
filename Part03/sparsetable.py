class Cell:
    def __init__(self, data):
        self.value = data
        
        
class SparseTable:
    def __init__(self):
        self.rows, self.cols = 0, 0
        self.cells = {}

    def __exist(self, row, col):
        row_exists, col_exists = False, False
        for key in self.cells:
            if row in key:
                row_exists = True
            if col in key:
                col_exists = True
            if row_exists and col_exists:
                break
        return row_exists, col_exists

    def add_data(self, row, col, value):
        # row_exists, con_exists = self.__exist(row, col)
        # self.rows += int(not row_exists)
        # self.cols += int(not con_exists)
        if row >= self.rows:
            self.rows = row + 1
        if col >= self.cols:
            self.cols = col + 1
        self.cells[(row, col)] = value

    def remove_data(self, row, col):
        if (row, col) not in self.cells:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.cells[(row, col)]
        # row_exists, con_exists = self.__exist(row, col)
        self.rows = max([key[0] for key in self.cells]) + 1
        self.cols = max([key[1] for key in self.cells]) + 1

    def __getitem__(self, item):
        if item not in self.cells:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[item]

    def __setitem__(self, key, value):
        self.add_data(*key, value)


# Test 1:
# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25  # изменение значения существующей ячейки
# st[11, 7] = 'cell_117'  # создание новой ячейки
# print(st[0, 0])  # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5]  # ValueError
# st.remove_data(12, 3)  # IndexError

# Test 2:
st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает " \
                       "инициализатор класса"
