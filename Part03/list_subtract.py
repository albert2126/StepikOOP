class NewList:
    def __init__(self, l: list = []):
        self.__lst = l

    def get_list(self):
        return self.__lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError(f'Incorrect type: cannot add list and {type(other)}')
        other = other if isinstance(other, list) else other.get_list()
        lst = self.__lst.copy()
        for item in other:
            for index in range(len(lst)):
                if (item, type(item)) == (lst[index], type(lst[index])):
                    del lst[index]
                    break
        return NewList(lst)

    def __rsub__(self, other):
        return NewList(other) - self

    def __isub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError(f'Incorrect type: cannot add list and {type(other)}')
        other = other if isinstance(other, list) else other.get_list()
        lst = self.__lst
        for item in other:
            for index in range(len(lst)):
                if (item, type(item)) == (lst[index], type(lst[index])):
                    del lst[index]
                    break
        return self


# Test 1:
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
# print(res_1.get_list(), res_2.get_list(), res_3.get_list(), res_4.get_list())

# Test 2:
lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
# print(lst1.get_list())
res1 = lst1 - lst2
res2 = lst1 - [0, True]
# print(lst1.get_list(), res2.get_list())
res3 = [1, 2, 3, 4.5] - lst2
# print(lst1.get_list(), lst2.get_list())
lst1 -= lst2
# print(lst1.get_list(), lst2.get_list())
assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# print(lst1.get_list(), res2.get_list())
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
