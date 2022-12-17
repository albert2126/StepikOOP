class TupleLimit(tuple):
    def __new__(cls, lst, max_limit):
        if len(lst) > max_limit:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return ' '.join(map(str, self))

    def __add__(self, other):
        return __class__(super().__add__(tuple(other)))


digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

try:
    tpl = TupleLimit(digits, 5)
except ValueError as e:
    print(e)
else:
    print(tpl)




# # Test:
# t = Tuple([1, 2, 3])
# t = t + "Python"
# print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# t = (t + "Python") + "ООП"



