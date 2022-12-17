from datetime import datetime

class DateError(Exception):
    pass

class DateString:
    def __init__(self, date_string):
        try:
            self.date = datetime.strptime(date_string, '%d.%m.%Y')
        except:
            raise DateError

    def __str__(self):
        return self.date.strftime('%d.%m.%Y')

date_string = input()
try:
    print(DateString(date_string))
except DateError:
    print("Неверный формат даты")
