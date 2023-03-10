class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls=Router):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)


# Test 1:
# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'
#
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)

# Test 2:
@Callback('/about', Router)
def about():
    return '<h1>About</h1>'


route = Router.get('/about')
ret = route()
assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

route = Router.get('/')
assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"
