# Runtime Errors

# My program hangs:
# Infinite loop
x = 10;
y = -10;

while x > 0 and y < 0:
    # do something to x
    # do something to y
    x = x - 1
    y = y + 1

    print('x: ', x)
    print('y: ', y)
    print("condition: ", (x > 0) and (y < 0))
