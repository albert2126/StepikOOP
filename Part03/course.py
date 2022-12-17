class LessonItem:
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __getattr__(self, key):
        return False

    def __setattr__(self, key, value):
        if key == 'title' and not isinstance(value, str) or \
           key in ('practices', 'duration') and not (isinstance(value, int) and value > 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        return False


class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if indx < len(self.lessons):
            del self.lessons[indx]


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if indx < len(self.modules):
            del self.modules[indx]


# Test 1:
course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
module_1.remove_lesson(1)
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
print(*(c.name for c in course.modules))
print(*(l.title for l in course.modules[0].lessons))
course.remove_module(1)
