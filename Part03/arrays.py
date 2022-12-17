class Integer:
    def __init__(self, start_value):
        self.__value = start_value
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__value = value


class Array:
    def __init__(self, max_length, cell=Integer):
        self.max_length = max_length
        self.cells = [cell(0) for _ in range(max_length)]

    def __isvalid(self, index):
        if not (isinstance(index, int) and 0 <= index <= self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
        return True

    def __getitem__(self, item):
        self.__isvalid(item)
        return self.cells[item].value

    def __setitem__(self, item, value):
        self.__isvalid(item)
        self.cells[item].value = value

    def __repr__(self):
        return ' '.join([str(c.value) for c in self.cells])


# Test:
ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение
print(ar_int)
