from abc import ABC, abstractmethod


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """Abstract method"""

    @abstractmethod
    def pop_back(self):
        """Abstract method"""


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
            return
        ob = self._top
        while ob._next:
            ob = ob._next
        ob._next = obj

    def pop_back(self):
        if not self._top:
            return
        if not self._top._next:
            obj = self._top
            self._top = None
            return obj
        prev = self._top
        obj = prev._next
        while obj._next:
            prev = obj
            obj = obj.next
        prev._next = None
        return obj


# Test 1:
st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(st.pop_back(), st.pop_back(), st.pop_back())
# print(st._top, st._top._next)

# Test 2:
assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"