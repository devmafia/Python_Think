import math

def mysqrt(a):
    x = 7;
    while True:
        print(x);
        y = (x + a/x) / 2;
        if y == x:
            break;
        x = y;

def test_square_root(a):
    print("a" + mysqrt(a));

def eval_loop():

    x = input(' :');
    while x != 'done':
        x = input('');
        

eval_loop('5');
