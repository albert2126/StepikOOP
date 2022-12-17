class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey (Monkeys):
    pass


class Person (Human):
    pass


class Flower (Flowering):
    pass


class Worm (Worms):
    pass


origin = """Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1"""

classes = Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys, Monkey, Person, Flower, Worm

lst_objs = []
for line in origin.split('\n'):
    cls_name, args = line.split(': ')
    cls = None
    for c in classes:
        if c.__name__ == cls_name:
            cls = c
            break
    args = args.split(', ')
    lst_objs.append(cls(args[0], float(args[1]), int(args[2])))

lst_animals = list(filter(lambda obj: isinstance(obj, Animals), lst_objs))
lst_plants = list(filter(lambda obj: isinstance(obj, Plants), lst_objs))
lst_mammals = list(filter(lambda obj: isinstance(obj, Mammals), lst_objs))


# Test:
print(lst_animals)
print(lst_plants)
print(lst_mammals)
