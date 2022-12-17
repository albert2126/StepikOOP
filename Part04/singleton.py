class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


# Test 1:
g1 = Game('Game 1')
g2 = Game('Game 2')
print(g1.name, g2.name)
print(id(g1), id(g2))
