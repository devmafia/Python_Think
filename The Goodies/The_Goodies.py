from collections import Counter
from collections import defaultdict
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
x, y = p

class Pointier(Point):
    #add more methods here
    def greeting(val):
        print(val)

def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, "3")
printall(1, 2.0, third="3")
d = dict(x = 1, y = 2)

# Conditional expressions

x = 0
if x > 0:
    y = math.log(x)
else:
    y = float('nan')

y = math.log(x) if x > 0 else float("nan")

def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n-1)

def factorial_2(n):
    return 1 if n == 0 else n * factorial(n-1)

class Kangoroo:

    def __init__(self, name, contents=None):
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    """
    def __init__(self, name, contents=None):
        self.name = name
        self.pouch_contents = [] if contents == None else contents
    """

# List comprehensions

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize_all())
    return res

def capitalize_all(t):
    return [s.capitalize_all() for s in t]

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

def only_upper(t):
    return [s for s in t if s.isupper()]

# Generator Expressions

g = (x ** 2 for x in range(5))

"""
for val in g:
    print(val)
"""

# any and all

any([False, False, True])

any(letter == 't' for letter in 'monty')

def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

def uses_all(word, required):
    return all(letter not in word for letter in required)

# Sets

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract_2(d1, d2):
    return set(d1) - set(d2)

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return True

def has_duplicates_2(t):
    return len(set(t)) < len(t)

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_only_2(word, available):
    return set(word) <= set(available)

# Counters

count = Counter("parrot")
var = count["d"]

"""
for val, freq in count.most_common(3):
    print(val, freq)
"""

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

def main():

    print(var)

    print(t)

# defaultdict

d = defaultdict(dict)
t = d["new key"]
t.append("new value")

def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d

def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number success

    return: int
    """

    if k == 0: 1 else if: n == 0: 0 else res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __self__(self):
        return "(%g, %g)" (self.x, self.y)

if __name__ == "__main__":
    main()
