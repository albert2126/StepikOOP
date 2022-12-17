class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, m):
        ylen, xlen = len(m), len(m[0])
        for row in m:
            if len(row) != xlen or not all(map(lambda x: isinstance(x, (int, float)), row)):
                raise ValueError("Неверный формат для первого параметра matrix.")
        xstep, ystep, xsize, ysize = (self.step + self.size)
        resxlen, resylen = xlen // xstep, ylen // ystep
        res = [[0] * resxlen for _ in range(resylen)]
        for y in range(resylen):
            for x in range(resxlen):
                x0, x1, y0, y1 = x * xstep, x * xstep + xsize, y * ystep, y * ystep + ysize
                res[y][x] = max([m[i][j] for i in range(y0, y1) if i < ylen
                                 for j in range(x0, x1) if j < xlen])
                # maxitem = -math.inf
                # for i in range(y * ystep, y * ystep + ysize):
                #     if i < ylen:
                #         for j in range(x * xstep, x * xstep + xsize):
                #             if j < xlen:
                #                 print(i, j)
                #                 if m[i][j] > maxitem:
                #                     maxitem = m[i][j]
                # res[y][x] = maxitem
        return res

# Test:
mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
print(res)
