class ListMath:
    
    def __init__(self, ls: list = []):
        self.lst_math = list(filter(lambda item: isinstance(item, (int, float)) and not isinstance(item, bool), ls))

    def __oper(self, other, op, right=False):       
        if not isinstance(other, (int, float)):
            raise TypeError(f'Incorrect type: {type(type(self))} cannot operate with {type(other)}')
        if right:
            cls = ListMath([other] * len(self.lst_math))
            return list(map(lambda x, y: eval(f"{str(x)} {op} {str(y)}"), cls.lst_math, self.lst_math))
        return list(map(lambda x: eval(f"{str(x)} {op} {str(other)}"), self.lst_math))

    def __add__(self, other):
        return ListMath(self.__oper(other, '+'))

    def __radd__(self, other):
        return ListMath(self.__oper(other, '+', True))

    def __iadd__(self, other):
        self.lst_math = self.__oper(other, '+')
        return self

    def __sub__(self, other):
        return ListMath(self.__oper(other, '-'))

    def __rsub__(self, other):
        return ListMath(self.__oper(other, '-', True))

    def __isub__(self, other):
        self.lst_math = self.__oper(other, '-')
        return self

    def __mul__(self, other):
        return ListMath(self.__oper(other, '*'))

    def __rmul__(self, other):
        return ListMath(self.__oper(other, '*', True))

    def __imul__(self, other):
        self.lst_math = self.__oper(other, '*')
        return self

    def __truediv__(self, other):
        return ListMath(self.__oper(other, '+'))

    def __rtruediv__(self, other):
        return ListMath(self.__oper(other, '+', True))

    def __idiv__(self, other):
        self.lst_math = self.__oper(other, '+')
        return self


# Test 1:
# lst = ListMath([1, "abc", -5, 7.68, True])
# print(lst.lst_math)
# lst = lst + 76  # сложение каждого числа списка с определенным числом
# print(lst.lst_math)
# lst = 6.5 + lst  # сложение каждого числа списка с определенным числом
# print(lst.lst_math)
# lst += 76.7  # сложение каждого числа списка с определенным числом
# print(lst.lst_math)

# Test 2:
lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
