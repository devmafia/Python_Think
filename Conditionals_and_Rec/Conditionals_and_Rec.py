import turtle

bob = turtle.Turtle()

def fermat_input():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    n = int(input("n:"))
    return check_fermat(a,b,c,n);

def check_fermat(a,b,c,n):
    if (pow(a,n) + pow(b,n)) == pow(c,n):
        return "No, that doesn't work";
    else:
        return "Holy smokes, Fermat was wrong";

#print(fermat_input());

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def koch(bob, length):
    if length < 10:
        bob.fd(length)
        return

    koch(bob, length/3)
    bob.lt(90)
    koch(bob, length/3)
    bob.rt(120)
    koch(bob, length/3)
    bob.lt(60)
    koch(bob, length/3)

def snowflake(bob, length):
    for i in range(3):
        koch(bob, length)
        bob.rt(120)

#draw(bob, 5, 5)
#koch(bob, 500)
snowflake(bob, 500)
