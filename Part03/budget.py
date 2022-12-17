class Item:
    def __init__(self, name, money):
        self.name = name 
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        return self.money + other

    def __radd__(self, other):
        return other + self.money


class Budget:
    def __init__(self):
        self.__items = []
 
    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, indx):
        del self.__items[indx]

    def get_items(self):
        return self.__items


# Test:
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
