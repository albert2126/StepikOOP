class Thing:
    ID = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None
        self.id = self.ID
        Thing.ID += 1

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


# Test 1:
th1 = Thing('my', 100)
th2 = Thing('second', 200)
print(th1.id, th2.id)
table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
