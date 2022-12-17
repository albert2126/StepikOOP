note_names = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
tones = (-1, 0, 1)


class Note:
    def __init__(self, name, ton):
        if name not in note_names or ton not in tones:
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in note_names or key == '_ton' and value not in tones:
            raise ValueError('недопустимое значение аргумента')
        self.__dict__[key] = value


class Notes:
    singleton = None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls)
        return cls.singleton

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        if item not in range(7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])

    def __setitem__(self, item, value):
        if item not in range(7):
            raise IndexError('недопустимый индекс')
        setattr(self, self.__slots__[item], value)


# Test:
notes = Notes()
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1  # изменение тональности ноты фа
print(*((n._name, n._ton) for n in notes))
# notes[1]._name = 'mm'
# notes[1]._ton = -2
