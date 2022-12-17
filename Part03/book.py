class Book:

    def __init__(self, title: str = '', author: str = '', pages: int | float = 0, year: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, attr, value):
        if attr in ('title', 'author') and not isinstance(value, str) or \
                attr in ('pages', 'year') and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, attr, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)

# Test:
print(book.__dict__)
