import math
import copy
import turtle

class Point:
    """Point in 2-D space"""

point_1 = Point();
point_1.x = 3;
point_1.y = 4;

point_2 = Point();
point_2.x = 5;
point_2.y = 5;

def distance_between_points(point1, point2):
    return math.sqrt(math.pow(int(point2.x-point1.x), 2)+math.pow(int(point2.y-point1.y), 2));

#print(distance_between_points(point_1, point_2));

class Rectangle:
    """Rectangle in 2-D space"""

box = Rectangle();
box.width = 300;
box.height = 200;
box.corner = Point();
box.corner.x = 0;
box.corner.y = 0;

def move_rectangle(rect, dx, dy):
    rect.corner.x = rect.corner.x + dx;
    rect.corner.y = rect.corner.y + dy;

def move_rectangle_copy(box, dx, dy):
    new_box = copy.deepcopy(box);
    new_box.corner.x = dx;
    new_box.corner.y = dy;
    return new_box;

move_rectangle(box, 50, 50);
#print(box.corner.x);

rect = move_rectangle_copy(box, 50, 50);
#print(rect.corner.x);

class Circle:
    """
    attributes: center, radius;
    """

circle = Circle();
circle.center = Point();
circle.center.x = 150;
circle.center.y = 100;

circle.radius = 75;

def point_in_circle(circ, p):

    d = distance_between_points(point, center.circle);
    print(d);
    return d <= circle.radius;

def rect_in_circle(circ, rectang):

    """points for rect_in"""
    left_up_point = Point();
    left_up_point.y = rectang.height;
    left_up_point.x = rectang.corner.x;
    right_up_point = Point();
    right_up_point.x = rectang.width;
    right_up_point.y = rectang.height;
    left_down_point = Point();
    left_down_point.x = 0;
    left_down_point.y = 0;
    right_down_point = Point();
    right_down_point.x = rectang.width;
    right_down_point.y = 0;

    if distance_between_points(left_up_point, circ.center) == distance_between_points(right_up_point, circ.center) == distance_between_points(left_down_point, circ.center) == distance_between_points(right_down_point, circ.center):
        return True;
    else:
        return False;

def rect_out_circle(circ, rectang):

    """points for rect_out"""
    left_mid_point = Point();
    left_mid_point.y = rectang.height/2;
    left_mid_point.x = rectang.corner.x;
    right_mid_point = Point();
    right_mid_point.x = rectang.width;
    right_mid_point.y = rectang.height/2;
    top_mid_point = Point();
    top_mid_point.x = rectang.width/2;
    top_mid_point.y = rectang.height;
    down_mid_point = Point();
    down_mid_point.x = rectang.width/2;
    down_mid_point.y = 0;

    if distance_between_points(left_mid_point, circ.center) == distance_between_points(right_mid_point, circ.center) == distance_between_points(top_mid_point, circ.center) == distance_between_points(down_mid_point, circ.center):
        return True;
    else:
        return False;

    #print(distance_between_points(left_mid_point, circ.center);

print(rect_out_circle(circle, box));

#def rect_circle_overlap(circ, rectang):
#    return;

bob = turtle.Turtle();

def draw_rect(t, rect):

    t.fd(rect.height);
    t.rt(90);
    t.fd(rect.width);
    t.rt(90);
    t.fd(rect.height);
    t.rt(90);
    t.fd(rect.width);

#draw_rect(bob, box);

def draw_circle(t, circ):

    circumference = 2 * math.pi * circ.radius;
    n = 50;
    length = circumference / n;
    angle = 360 / n;
    for i in range(n):
        t.fd(length);
        t.lt(angle);

#draw_circle(bob, circle);
