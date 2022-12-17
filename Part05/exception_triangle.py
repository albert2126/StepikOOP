class Triangle:
    def __init__(self, a, b, c):
        if any(map(lambda y: y <= 0, (a, b, c))):
            raise TypeError('стороны треугольника должны быть положительными числами')
        if a > b + c or b > a + c or c > a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')
        self.a = a
        self.b = b
        self.c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for x in input_data:
    try:
        lst_tr.append(Triangle(*x))
    except (TypeError, ValueError):
        continue


# Test:
print(lst_tr)

