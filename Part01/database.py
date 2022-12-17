import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        self.lst_data += [dict(zip(self.FIELDS, d.split())) for d in data]

    def select(self, a, b):
        b = min(b, len(self.lst_data))
        return self.lst_data[a: b + 1]


db = DataBase()
db.insert(lst_in)

# Tests
print(db.__dict__)