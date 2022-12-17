class ObjList:
    def __init__(self, data: str):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if not self.tail:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if not self.tail:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        if self.tail is None:
            return []
        obj = self.head
        data_list = [obj.get_data()]
        while obj.get_next():
            obj = obj.get_next()
            data_list.append(obj.get_data())
        return data_list


# Test1:
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# print(*res, sep='\n')

# Test2:

ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
ls_one_data = ls_one.get_data()
assert ls_one_data == [1], "метод get_data вернул неверные данные: " + str(ls_one_data)

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает " \
                                "метод remove_obj"

ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"

h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"

h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"
