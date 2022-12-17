class AppVK:
    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:
    def __init__(self, memory):
        self.name = 'YouTube'
        self.memory = memory


class AppPhone:
    def __init__(self, phone_list: dict):
        self.name = 'Phone'
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if not any((type(a) == type(app) for a in self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            del self.apps[self.apps.index(app)]

# Test 1:
app_1 = AppVK() # name = "ВКонтакте"
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами

# Test 2:
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
