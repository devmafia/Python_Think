from datetime import datetime

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

now = datetime.now()

class Time:
    """Represents the time of day"""

    def __init__(self, hour=0, minute=0, second=0):
        self.seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    def print_time_inside(self):
        time_arr = int_to_time(self.seconds_since_midnight).split(':')
        print(time_arr)

    def time_to_int(self):
        return self.seconds_since_midnight

    def int_to_time(self, seconds):
        minutes, second = divmod(seconds, 60);
        hour, minute = divmod(minutes, 60);
        return ('%.2d:%.2d:%.2d' % (hour, minute, second));

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

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

    def __str__(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time):
    print(int_to_time(self.seconds_since_midnight).split(':'))

class Point:
    """Point in 2-D space"""

point_1 = Point()
point_1.x = 3
point_1.y = 4

attributes = vars(point_1)
point_1_x = getattr(point_1, 'x')

class Kangoroo:
    """The well-known animal"""

    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

kango = Kangoroo("Kango")
roo = Kangoroo("Roo")

kango.put_in_pouch(roo)
print(kango)
