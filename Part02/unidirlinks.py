class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if not self.top:
            # print(f"1: {obj.data}")
            self.top = self.tail = obj
        else:
            # print(f"2: {obj.data}")
            self.tail.next = obj
            self.tail = obj

    def pop(self):
        if not self.top:
            return
        if self.top == self.tail:
            obj = self.top
            self.top = self.tail = None
            return obj
        prev, obj = None, self.top
        while obj.next:
            prev, obj = obj, obj.next
        prev.next = None
        self.tail = prev

    def get_data(self):
        # print(self.top, self.tail)
        if not self.top:
            # print('4: No objects')
            return []
        obj = self.top
        data_lst = [self.top.data]
        while obj.next:
            # print(f"5: {obj}")
            obj = obj.next
            data_lst.append(obj.data)
        return data_lst


# Test:
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# print(res)
#
# Test 2:
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
