import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = {}
for i in lst_in:
    its = i.split()
    item = ShopItem(its[0].rstrip(':'), its[1], its[2])
    if item not in shop_items:
        shop_items[item] = [item, 1]
    else:
        num = shop_items.get(item)[1] + 1
        shop_items[item] = [item, num]


# Test:
print(shop_items)
