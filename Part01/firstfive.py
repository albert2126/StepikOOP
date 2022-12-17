class SingletonFive:
    __ObjCount = 5
    __Singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.__ObjCount > 0:
            cls.__ObjCount -= 1
            cls.__Singleton = super().__new__(cls)
            return cls.__Singleton
        else:
            return cls.__Singleton

    def __init__(self, name):
        print(f'Assigning name {name} to object {self}')
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять

print(*((id(ob), ob.name) for ob in objs), sep='\n')
