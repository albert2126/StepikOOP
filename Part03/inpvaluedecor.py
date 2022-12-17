import re


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.render(w) for w in func().split()]
        return wrapper


class RenderDigit:
    def __call__(self, string: str):
        if re.fullmatch(r'-?\d+$', string):
            return int(string)


render = RenderDigit()


@InputValues(render)
def input_dg():
    return input()


res = input_dg()
print(res)
