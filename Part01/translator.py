class Translator:
    data = {}

    def add(self, eng: str, rus: str):
        self.data[eng] = self.data.setdefault(eng, [])
        if rus not in self.data[eng]:
            self.data[eng].append(rus)

    def remove(self, eng: str):
        if eng in self.data:
            del self.data[eng]

    def translate(self, eng: str) -> list[str]:
        return self.data.get(eng, [])


# Tests:

data = """tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко"""

tr = Translator()
for e, r in (d.split(' - ') for d in data.split('\n')):
    tr.add(e, r)
tr.remove('car')
print(*tr.translate('go'))

print(tr.translate('tree')[0])
print(tr.translate('digits'))