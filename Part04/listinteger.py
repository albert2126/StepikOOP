class ListInteger(list):
    @classmethod
    def _is_listint(cls, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, data):
        for x in data:
            self._is_listint(x)
        super().__init__(data)

    # def __getitem__(self, item):
    #     return self.data[item]

    def __setitem__(self, key, value):
        self._is_listint(value)
        super().__setitem__(key, value)

    def append(self, value):
        self._is_listint(value)
        super().append(value)

    # def __str__(self):
    #     return f"[{', '.join(map(str, self.data))}]"

# Test:
s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5  # TypeError
