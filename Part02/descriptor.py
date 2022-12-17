class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, v=0.0):
        self.value = v


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)
table.cells = [[Cell(float(i + j * 3)) for i in range(1, 4)] for j in range(0, 5)]


# Test:
# print(table.cells)

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
