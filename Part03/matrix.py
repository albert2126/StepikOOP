class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            if not all((isinstance(x, (int, float)) for x in args)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.table = [[args[2] for _ in range(args[1])] for _ in range(args[0])]
            self.__rows = args[0]
            self.__cols = args[1]
        else:
            if not isinstance(args[0], list) \
                    or len(list(filter(lambda r: len(r) == len(args[0][0]), args[0]))) != len(args[0])\
                    or not all((isinstance(x, (int, float)) for r in args[0] for x in r)):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.table = args[0]
            self.__rows = len(self.table)
            self.__cols = len(self.table[0])

    def __check_index(self, index):
        i, j = index
        if not (isinstance(i, int) and 0 <= i < self.__rows and isinstance(i, int) and 0 <= j < self.__cols):
            raise IndexError('недопустимые значения индексов')

    def __check_size(self, other):
        if not (self.__rows == len(other.table) and self.__cols == len(other.table[0])):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.table[item[0]][item[1]]

    def __setitem__(self, item, value):
        self.__check_index(item)
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        self.table[item[0]][item[1]] = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            m = [[self[i, j] + other for j in range(self.__cols)] for i in range(self.__rows)]
        else:
            self.__check_size(other)
            m = [[self[i, j] + other[i, j] for j in range(self.__cols)] for i in range(self.__rows)]
        return Matrix(m)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            m = [[self[i, j] - other for j in range(self.__cols)] for i in range(self.__rows)]
        else:
            self.__check_size(other)
            m = [[self[i, j] - other[i, j] for j in range(self.__cols)] for i in range(self.__rows)]
        return Matrix(m)


# Test:
mt = Matrix([[1, 2], [3, 4]])
res1 = mt[0, 0] # 1
res2 = mt[0, 1] # 2
res3 = mt[1, 0] # 3
# print(res1, res2, res3)
mt1 = Matrix([[1, 2], [3, 4]])
mt2 = mt + mt1
print(mt2.table)

