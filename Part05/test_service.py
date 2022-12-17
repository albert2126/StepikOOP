class Test:
    def __init__(self, descr: str):
        if not isinstance(descr, str) or not 10 <= len(descr) <= 10_000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr: str, ans_digit: float, max_error_digit: float = 0.01):
        super().__init__(descr)
        if not isinstance(ans_digit, (int, float)) or not isinstance(max_error_digit, float) or\
           not 0 <= max_error_digit:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return abs(self.ans_digit - ans) <= self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)
try:
    test = TestAnsDigit(descr, ans)
    print(test.run())
except (NotImplementedError, ValueError) as e:
    print(e)


# test:
try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором " \
                  "аргументов"

try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False
