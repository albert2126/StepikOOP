s_inp = input()  # эту строку (переменную s_inp) в программе не менять

class Dimensions:
    def __init__(self, a, b, c):
        if not all([item > 0 for item in (a, b, c)]):
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst_dims = sorted([Dimensions(*[float(i) for i in dim.split()]) for dim in s_inp.split(';')], key=lambda x: hash(x))


# Test:
print(*[hash(i) for i in lst_dims])
