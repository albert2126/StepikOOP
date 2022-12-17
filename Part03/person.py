class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job =year_job
        self.keys = ['fio', 'job', 'old', 'salary', 'year_job']
        self.__length = 5
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= self.__length:
            raise StopIteration
        self.__index += 1
        return list(self.__dict__.values())[self.__index - 1]

    def __getitem__(self, item):
        if not (isinstance(item, int) and 0 <= item < self.__length):
            raise IndexError('неверный индекс')
        return list(self.__dict__.values())[item]

    def __setitem__(self, item, value):
        if not (isinstance(item, int) and 0 <= item < self.__length):
            raise IndexError('неверный индекс')
        setattr(self, self.keys[item], value)


# Test:
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers.__dict__)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
