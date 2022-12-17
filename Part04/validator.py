class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        # super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        # super().__init__()
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_value <= data <= self.max_value


# Test:
integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError
