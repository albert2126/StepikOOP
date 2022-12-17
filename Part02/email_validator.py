from random import choice, choices
from string import ascii_letters, digits


class EmailValidator:
    symbols = ascii_letters + digits + '_.'

    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        pre_len = choice(range(1, 100))
        post_len = choice(range(2, 50))
        dot_pos = choice(range(1, post_len - 1))
        pre = ''.join(choices(cls.symbols + '.', k=pre_len))
        post = ''.join(choices(cls.symbols, k=post_len - 1))
        post = post[:dot_pos] + '.' + post[dot_pos:]
        email = pre + '@' + post
        if not cls.check_email(email):
            return cls.get_random_email()
        return email

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email) or len(email.split('@')) != 2:
            return False
        pre, post = email.split('@')
        if set(pre + post) & set(cls.symbols) != set(pre + post):
            return False
        if len(pre) > 100 or len(post) > 50 or '.' not in post or '..' in pre + post:
            return False
        return True

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


# Test:

assert EmailValidator.check_email("sc_lib@list.ru") == True, '1'
assert EmailValidator.check_email("sc_lib@list_ru") == False, '2'
assert EmailValidator.check_email("sc@lib@list_ru") == False, '3'
assert EmailValidator.check_email("sc.lib@list_ru") == False, '4'
assert EmailValidator.check_email("sclib@list.ru") == True, '5'
assert EmailValidator.check_email("sc.lib@listru") == False, '6'
assert EmailValidator.check_email("sc..lib@list.ru") == False, \
    "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
# print(m)
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
