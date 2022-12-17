# class TeleProp:
#     def __set_name__(self, owner, name):
#         self.name = '__id' if name == 'uid' else '__' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#

class Telecast:
    def __init__(self, uid: int, title: str, duration: int):
        self.__id = uid
        self.__name = title
        self.__duration = duration

    @property
    def uid(self):
        return self.__id
    
    @uid.setter
    def uid(self, uid):
        # self.__id = uid
        # self.uid = uid
        # setattr(self, '_Telecast__id', uid)
        setattr(self, '_' + self.__class__.__name__ + '__id', uid)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, channel: str):
        self.channel_name = channel
        self.items = []

    def add_telecast(self, tl: Telecast):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for index in range(len(self.items)):
            if self.items[index].uid == indx:
                del self.items[index]
                break


# Test 1:
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(2, "Новости", 2000))
# pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")

# Test 2:
assert hasattr(TVProgram, 'add_telecast') and hasattr(TVProgram, 'remove_telecast'), "в классе TVProgram должны быть методы add_telecast и remove_telecast"

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

print(pr.items[0].__dict__)
pr.remove_telecast(3)
assert len(pr.items) == 2, "неверное число телеперач, возможно, некорректно работает метод remove_telecast"
assert pr.items[-1] == t, "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"

# print(Telecast.uid)
assert type(Telecast.uid) == property
assert type(Telecast.name) == property
assert type(Telecast.duration) == property, "в классе Telecast должны быть объекты-свойства uid, name и duration"

for x in pr.items:
    assert hasattr(x, 'uid') and hasattr(x, 'name') and hasattr(x, 'duration')

assert pr.items[0].name == "Доброе утро", "объект-свойство name вернуло неверное значение"
assert pr.items[0].duration == 10000, "объект-свойство duration вернуло неверное значение"

t = Telecast(1, "Доброе утро", 10000)
t.uid = 20
t.name = "hello"
t.duration = 10
print(t.uid)