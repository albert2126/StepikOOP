class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        keys = list(self.__dict__.keys())
        return getattr(self, keys[key])

    def __setitem__(self, key, value):
        if not (isinstance(key, int) and 0 <= key < len(self.__dict__)):
            raise IndexError('неверный индекс поля')
        keys = list(self.__dict__.keys())
        setattr(self, keys[key], value)


# Test:
r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)

r.pk # 1
r.title # Python ООП
r.author # Балакирев

r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
list((1,2,3))
