def class_log(log_lst):
    def method_log(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    def class_renewal(cls):
        [setattr(cls, k, method_log(v)) for k, v in cls.__dict__.items() if callable(v)]
        return cls

    return class_renewal


# здесь объявляйте декоратор и все что с ним связано
vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


# Test
