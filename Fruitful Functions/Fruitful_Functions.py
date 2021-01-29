def ack(m, n):
    if m == 0:
        return n + 1;
    if m > 0 and n == 0:
        return ack(m-1, 1);
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1));

# print(ack(3, 4));

def first(word):
    return word[0];

def last(word):
    return word[-1];

def middle(word):
    return word[1:-1];

# print(middle(''));

def is_polindrome(word):
    if len(word) == 1:
        return True;
    if first(word) != last(word):
        return False;
    return is_polindrome(middle(word));
print(is_polindrome('hoooh'));
