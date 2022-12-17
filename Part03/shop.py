class Product:
    incr_id = iter(range(1, 1000))

    def __init__(self, name: str, weight: float, price: float):
        self.id = next(self.incr_id)
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and not isinstance(value, str) or \
                key in ('price', 'weight') and not (isinstance(value, (int, float)) and value >= 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, key)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            index = self.goods.index(product)
            self.goods.pop(index)


# Test:
shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
