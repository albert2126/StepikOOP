class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return (self.name.lower(), self.mass) == (other.name.lower(), other.mass)

    def __lt__(self, other):
        return (self.name.lower(), self.mass) < (other.name.lower(), other.mass)

    # def __le__(self, other):
    #     return (self.name.lower(), self.mass) <= (other.name.lower(), other.mass)


class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        return sorted(self.things) == sorted(other.things)



# Test:
b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)
