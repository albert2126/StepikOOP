import sys


class Record:
    PK = 0
    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = Record.PK
        Record.PK += 1

    def __hash__(self):
        return hash((self.fio, self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

    
class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        return next(filter(lambda item: item.pk == pk, self.dict_db), None)


lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase('321')
for line in lst_in:
    args = line.split('; ')
    db.write(Record(args[0], args[1], args[2]))

# Test:
db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == int(r2.old), "при операциях write и " \
                                                                                              "read прочитанный " \
                                                                                              "объект имеет неверные " \
                                                                                              "значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"
