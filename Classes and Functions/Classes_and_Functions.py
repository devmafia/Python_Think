from datetime import datetime

class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

time1 = Time();
time1.hour = 11;
time1.minute = 9;
time1.second = 30;

def print_time(time):
    return '%02d' % time.hour+':'+'%02d' % time.minute+':'+ '%02d' % time.second;

time2 = Time();
time2.hour = 19;
time2.minute = 50;
time2.second = 55;

#print(print_time(time1));

def time_to_int(time):
    minutes = time.hour * 60 + time.minute;
    seconds = minutes * 60 + time.second;
    return seconds;

def int_to_time(seconds):
    time = Time();
    minutes, time.second = divmod(seconds, 60);
    time.hour, time.minute = divmod(minutes, 60);
    return time;

def is_after(t1, t2):
    time1_in_seconds = t1.hour*3600+t1.minute*60+t1.second;
    time2_in_seconds = t2.hour*3600+t2.minute*60+t2.second;
    if (time1_in_seconds-time2_in_seconds)>0:
        return True;
    else:
        return False;

#print(is_after(time1, time2));

def mul_time(t, num):
    time = Time();
    time1_in_seconds = t.hour*3600+t.minute*60+t.second;
    time = int_to_time(time1_in_seconds);
    return time;

current_time = datetime.now();
print(current_time);

def day_of_the_week(cur_time):
    return cur_time.day;

#print(day_of_the_week(current_time));

"""
    1. make a validation function for
"""

#birth = input("input your birthday in format: mm/dd/yyyy");

def until_the_next_birth(birthday):
    s = birthday;
    s = '5/11/1967'
    bday = datetime.strptime(s, '%m/%d/%Y')

    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)

    until_next_bday = next_bday - today

#print(until_the_next_birth(birth));

def double_day():
    """
        1. We have 2 birthdays
        2. the double day becomes when one is twice older than the other
    """
    print("For people born on these dates:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)


    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    print(d2 - d1)
    dd = d2 + (d2 - d1)
    return dd;

def n_times_older(number):
    """
        1. We have 2 birthdays
        2. the double day becomes when one is twice older than the other
    """
    print("For people born on these dates:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)


    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + number*(d2 - d1)
    return dd;

print(n_times_older(5));
