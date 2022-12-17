class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.tail:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def remove_obj(self, indx):
        if not self.tail:
            return
        if self.head == self.tail and indx == 0:
            self.tail = self.head = None
            return
        count, obj = 0, self.head
        while obj.next:
            if count == indx:
                if not obj.prev:
                    obj.next.prev = None
                    self.head = obj.next
                else:
                    obj.prev.next = obj.next
                    obj.next.prev = obj.prev
                return
            count += 1
            obj = obj.next
        if count == indx:
            obj.prev.next = None
            self.tail = obj.prev

    def __len__(self):
        if not self.tail:
            return 0
        count, obj = 1, self.head
        while obj.next:
            count += 1
            obj = obj.next
        return count

    def __call__(self, indx):
        if not self.tail:
            return
        count, obj = 0, self.head
        while obj.next:
            if count == indx:
                return obj.data
            count += 1
            obj = obj.next
        if count == indx:
            return obj.data


# Test 1:
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# print([linked_lst(i) for i in range(3)])
# print([linked_lst.head, linked_lst.head.next, linked_lst.head.next.next, linked_lst.head.next.next.next])
# print([linked_lst.head.prev, linked_lst.head.next.prev, linked_lst.head.next.next.prev, linked_lst.tail])
#
# linked_lst.remove_obj(2)
# print([linked_lst(i) for i in range(3)])
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1)  # s = Balakirev
# print(n, s)

# Test 2:
ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(
    ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"

