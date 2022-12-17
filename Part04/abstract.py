from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """pass"""

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = 1
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = __class__._id
        __class__._id += 1

    def get_pk(self):
        return self._id


# Test:
form = ModelForm("Логин", "Пароль")
print(form.get_pk())
print(ModelForm('bbb', '111').get_pk())
