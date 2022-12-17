class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

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


class Stack:
    def __init__(self):
        self.top = None

    def __validate(self, index):
        if not (isinstance(index, int) or 0 <= index) or (not self.top and index > 0):
            raise IndexError('неверный индекс')

    def push_front(self, obj):
        if not self.top:
            self.top = obj
            return
        obj.next, self.top = self.top, obj

    def push_back(self, obj):
        if not self.top:
            self.top = obj
            return
        ob = self.top
        while ob.next:
            ob = ob.next
        ob.next = obj

    def pop(self):
        if not self.top:
            return
        ob = self.top
        if not ob.next:
            self.top = None
        prev = ob
        while ob.next:
            prev, ob = ob, ob.next
        prev.next = None
        return ob

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, lst):
        for data in lst:
            self.push_back(StackObj(data))
        return self

    def __get_item(self, index):
        self.__validate(index)
        ob = self.top
        for i in range(index):
            if ob.next is None:
                raise IndexError('неверный индекс')
            ob = getattr(ob, 'next', None)
        return ob

    def __getitem__(self, item):
        return self.__get_item(item).data

    def __setitem__(self, index, value):
        self.__get_item(index).data = value

    def __len__(self):
        count, obj = 0, self.top
        while obj:
            count += 1
            obj = obj.next
        return count

    def __iter__(self):
        for i in range(len(self)):
            yield self.__get_item(i)

# Test 1:
# assert hasattr(Stack, 'pop'), "класс Stack должен иметь метод pop"
#
# st = Stack()
# top = StackObj("1")
# st.push(top)
# assert st.top == top, "неверное значение атрибута top"
#
# st = st + StackObj("2")
# st = st + StackObj("3")
# obj = StackObj("4")
# st += obj
#
# st = st * ['data_1', 'data_2']
# st *= ['data_3', 'data_4']
#
# d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
# h = top
# i = 0
# while h:
#     assert h._StackObj__data == d[
#         i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
#     h = h._StackObj__next
#     i += 1
#
# assert i == len(d), "неверное число объектов в стеке"


# Test 2:
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data)  # obj3
# print(st[1].data)  # new obj2
# res = st[3]  # исключение IndexError
# print(res.data)


# Test 3:
# st = Stack()
# st.push_back(StackObj("obj11"))
# st.push_back(StackObj("obj12"))
# st.push_back(StackObj("obj13"))
# st[1] = StackObj("obj2-new")
# assert st[0].data == "obj11" and st[
#     1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"
#
# try:
#     obj = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# obj = st.pop()
# assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"
#
# n = 0
# h = st.top
# while h:
#     assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
#     n += 1
#     h = h.next
#
# assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

# Test 4:
st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
