from datetime import datetime

class Time:
    """Represents the time of day"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour;
        self.minute = minute;
        self.second = second;

    def print_time_inside(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second));

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute;
        seconds = minutes * 60 + self.second;
        return seconds;

    def is_after(self, other):
        return self.time_to_int() > self.other.time_to_int();

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second));


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

now = datetime.now()

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second));


class Point:
    """Point in 2-D space"""

point_1 = Point();
point_1.x = 3;
point_1.y = 4;

attributes = vars(point_1)
point_1_x = getattr(point_1, 'x')

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
