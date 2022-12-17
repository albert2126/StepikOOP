import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

lst_bs = [BookStudy(*line.split('; ')) for line in lst_in]
unique_books = len(set((hash(obj) for  obj in lst_bs)))


# Test:
print(lst_bs)
print(*[hash(obj) for obj in lst_bs])
print(unique_books)
