class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for row in self.lst:
            yield from row


class IterColumn:
    def __init__(self, lst, column):
            self.lst = lst
            self.column = column

    def __iter__(self):
        yield from (self.lst[x][self.column] for x in range(len(self.lst)))


# Test 1:

# ls = [['x00'],
#        ['x10', 'x11'],
#        ['x20', 'x21', 'x22'],
#        ['x30', 'x31', 'x32', 'x33']]
#
# it = TriangleListIterator(ls)
# it_iter = iter(it)
# x = next(it_iter)
# print(x)
# print(next(it_iter))
# print(next(it))

# Test 2:
lst = [['x11', 'x12', 'x1N'],
       ['x21', 'x22', 'x2N'],
       ['xM1', 'xM2', 'xMN']]
it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
print(x)




