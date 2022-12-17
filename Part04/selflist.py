class SoftList(list):
    def __getitem__(self, index):
        if not super().__len__() * -1 <= index < super().__len__():
            return False
        return super().__getitem__(index)


# Test:
sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False
print(sl)
print(sl[7])
print(sl[-7], sl[-6])
