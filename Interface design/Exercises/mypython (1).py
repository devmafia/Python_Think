import math
import copy

class Point:
    """Point in 2-D space"""
    def __init__(self, X=0, Y=0):
        self.x = X
        self.y = Y

    def distance_to_point(self, point):
        return math.sqrt(math.pow(point.x-self.x, 2)+math.pow(point.y-self.y, 2));

    def toString(self):
        return "("+str(self.x)+", "+str(self.y)+")";

def distance_between_points(point1, point2):
        return math.sqrt(math.pow(point2.x-point1.x, 2)+math.pow(point2.y-point1.y, 2));

point_1 = Point();
point_1.x = 3;
point_1.y = 4;

point_2 = Point();
point_2.x = 5;
point_2.y = 5;

#print(distance_between_points(point_1, point_2));

class Rectangle:
    """Rectangle in 2-D space"""
    def __init__(self, Width=0, Height=0, corner_x=0, corner_y=0):
        self.width = Width
        self.height = Height
        self.x = corner_x
        self.y = corner_y
        self.corner = Point(corner_x,corner_y)


    def move_rectangle(self, dx, dy):
        self.corner.x = self.corner.x + dx;
        self.corner.y = self.corner.y + dy;

    def move_rectangle_copy(self, dx, dy):
        new_box = copy.deepcopy(self);
        new_box.move_rectangle(dx,dy)
        return new_box;

box = Rectangle();
box.width = 300;
box.height = 200;
box.corner = Point();
box.corner.x = 0;
box.corner.y = 0;

#print(box.corner.x);

#rect = box.move_rectangle_copy();
#print(rect.corner.x);

class Circle:
    """
    attributes: center, radius;
    """
    def __init__(self, X=0, Y=0, Radius=0):
        self.center = Point(X,Y)
        self.radius = Radius

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
    left_up_point = Point(rectang.y+rectang.height, rectang.corner.x);

    right_up_point = Point(rectang.x+rectang.width, rectang.y+rectang.height);

    left_down_point = Point(rectang.x, rectang.y);

    right_down_point = Point(rectang.x+rectang.width, rectang.y);

    if distance_between_points(left_up_point, circ.center) == distance_between_points(right_up_point, circ.center) == distance_between_points(left_down_point, circ.center) == distance_between_points(right_down_point, circ.center) and distance_between_points(left_up_point, circ.center) <= circ.radius:
        return True;
    else:
        return False;


def rect_out_circle(circ, rectang):

    """points for rect_out"""
    left_mid_point = Point(rectang.corner.x, rectang.y+rectang.height/2);

    right_mid_point = Point(rectang.x+rectang.width, rectang.y+rectang.height/2);

    top_mid_point = Point(rectang.x+rectang.width/2, rectang.y+rectang.height);

    down_mid_point = Point(rectang.x+rectang.width/2, rectang.y);

    if distance_between_points(left_mid_point, circ.center) == distance_between_points(right_mid_point, circ.center) == distance_between_points(top_mid_point, circ.center) == distance_between_points(down_mid_point, circ.center)  and distance_between_points(left_up_point, circ.center) >= circ.radius:
        return True;
    else:
        return False;

print(rect_in_circle(circle, box));
print(rect_out_circle(circle, box));

#def rect_circle_overlap(circ, rectang):
#    return;
