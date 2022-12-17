class IteratorAttrs:
    name = 'IteratorAttrs'
    def __iter__(self):
        yield from self.__dict__.items()


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


# Test:
phone = SmartPhone('model', (4, 5), 2000)
for attr, value in phone:
    print(attr, value)
