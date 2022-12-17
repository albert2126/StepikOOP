class InputDigits:
    def __init__(self, func):
        self.__fn = func

    def __call__(self):
        return [int(i) for i in self.__fn().split()]


@InputDigits
def input_dg():
    return input()


res = input_dg()


# Test:
print(res)
