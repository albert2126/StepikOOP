TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    obj = None
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        elif TYPE_OS == 2:
            obj = super().__new__(DialogLinux)
        setattr(obj, 'name', args[0])
        return obj

    # def __init__(obj, name):
    #     obj.name = name

# Test:
d = Dialog('d1')
print(type(d), d.__dict__)

