class CellException(Exception):
    pass


class CellIntegerException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellFloatException(CellException):
    def __str__(self):
        return 'значение выходит за допустимый диапазон'


class CellStringException(CellException):
    def __str__(self):
        return 'длина строки выходит за допустимый диапазон'


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) != int or not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._value = value


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) != float or not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._value = value



class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) != str or not self._min_length <= len(value) <= self._max_length:
            raise CellStringException('значение выходит за допустимый диапазон')
        self._value = value


class TupleData:
    def __init__(self, *args):
        self.cells = list(args)

    def __getitem__(self, item):
        if item not in range(len(self.cells)):
            raise IndexError
        return self.cells[item].value

    def __setitem__(self, item, value):
        if item not in range(len(self.cells)):
            raise IndexError
        self.cells[item].value = value

    def __len__(self):
        return len(self.cells)


# Test:
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    # ld[3] = ''
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
