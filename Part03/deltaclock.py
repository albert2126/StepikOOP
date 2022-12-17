class Clock:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def get_time(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __str__(self):
        delta = len(self)
        return f"{delta // 3600:02d}: {delta % 3600 // 60:02d}: {delta % 60:02d}"

    def __len__(self):
        delta = self.__clock1.get_time() - self.__clock2.get_time()
        return delta if delta >= 0 else 0


# Test 1:
dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt) # 5400
