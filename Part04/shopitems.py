class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __init__(self):
        super().__init__()

    def __str__(self):
        return '\n'.join([f"{k}: {v}" for k, v in self.__dict__.items()])


class ShopUserView:
    def __init__(self):
        super().__init__()

    def __str__(self):
        return '\n'.join([f"{k}: {v}" for k, v in self.__dict__.items() if k != '_id'])


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


# Test 1:
class Book1(Book, ShopItem, ShopGenericView):...
book = Book1("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022

# Test 2:
class Book2(Book, ShopItem, ShopUserView): ...
book = Book2("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _title: Python ООП
# _author: Балакирев
# _year: 2022