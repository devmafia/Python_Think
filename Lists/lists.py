from random import randint

t = [[1,2],[3],[4,5,6]];

def nested_sum(t):
    w = 0;
    for i in t:
        for c in i:
            w += c
    return w;

print(nested_sum(t));

t = [1,2,3];


def cumsum(t):
    w = [];
    r = 0;
    for q in t:
        r += q;
        w.append(r);

    return w;


print(cumsum(t));

t = [1,2,3,4];

def middle(t):
    w = [];
    for i in range(len(t)):
        if (i == 1) or (i == 2):
            w.append(t[i]);
    return w;

print(middle(t));

t = [1,2,3,4];

"""
    for i in range(len(t)):
        print(t[i]);
        if (i == 0) or (i == 1):
            t.pop(i)
"""

def chop(t):

    del t[0];
    del t[-1];

chop(t);

def is_sorted(t):

    return t == sorted(t);
    # iterate over and compare
    # save previous
    # compare with the next

print(is_sorted(t));

t = [1,2,3,4];

def has_duplicates(s):

    t = list(s);
    t.sort();

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True;
    return False;

print(has_duplicates(t));

words = open('words.txt');

t = [1,2,3,4];

def random_bdays(students):

    t = [];

    for i in range(23):
        t.append(randint(0, 365));
    return t;

print(random_bdays(23));

def wordlist_1():
    file = open('words.txt');

    q = [];

    for line in file:
        q.append(line.strip());

    print(q);

#wordlist_1();

def wordlist_2():
    file = open('words.txt');

    q = [];

    for line in file:
        q = q + [line.strip()];

    print(q);

wordlist_2();

def bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False;

    i = len(word_list) // 2
    if word_list[i] == word:
        return word_list[];

    if word_list[i] > word:
        # search the first half
        return bisect(word_list[:i], word)
    else:
        # search the second half
        return bisect(word_list[i+1:], word)

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
