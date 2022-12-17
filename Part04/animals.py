class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


# Test:
dog = Dog('name', 7, 'овчарка', (5, 7))
assert dog.name == 'name' and dog.old == 7 and dog.breed == 'овчарка' and dog.size == (5, 7), "неверные значения атрибутов объекта класса Dog"

cat = Cat('cat', 5, 'green', 2)
assert cat.get_info() == 'cat: 5, green, 2', "метод get_info вернул неверные данные"
