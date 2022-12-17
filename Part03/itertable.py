class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.__table = [[Cell(0) for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols
        self.__type = type_data

    def __validate(self, index):
        x, y = index
        if not (isinstance(x, int) and 0 <= x < self.__rows) \
                or not (isinstance(y, int) and 0 <= y < self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__validate(item)
        return self.__table[item[0]][item[1]].data

    def __setitem__(self, item, value):
        self.__validate(item)
        if not isinstance(value, self.__type):
            raise TypeError('неверный тип присваиваемых данных')
        self.__table[item[0]][item[1]].data = value

    def __iter__(self):
        for row in self.__table:
            yield (cell.data for cell in row)

# Test:
tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, " \
                                          "должен сначала возвращаться итератор для строк, а затем, этот итератор " \
                                          "должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
