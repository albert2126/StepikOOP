class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        self.rows, self.cols, self.cell = rows, cols, cell
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, coord):
        return self.cells[coord[0]][coord[1]].value

    def __setitem__(self, coord, value):
        self.cells[coord[0]][coord[1]].value = value


# Test:
table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
