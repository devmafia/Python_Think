
def make_list():
    file = open('words.txt');

    d = {};

    for i,line in enumerate(file):
        d[line.strip()] = i;

    return d;

wordlist = make_list();

dictionary = {'a': 1, 'p': 1,'r': 2,'t': 1, 'o':1};

def invert_dict_2(d):
    invert = dict()

    for key in d:
        val = d[key];
        invert.setdefault(val, []).append(key);

    return invert;

#print(invert_dict_2(dictionary));

"""
1. create dict
2. loop over the paramter
3. d.setdefault("");
"""

def invert_dict_1(d):
    invert = dict();
    for key in d:
        val = d[key]
        print(val);
        if val not in invert:
            invert[val] = [key];
        else:
            invert[val].append(key);
    return invert;

#invert_dict_1(dictionary);

def has_duplicates(s):
    t = list(s);
    t.sort();

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True;
    return False;

dictionary = {'a': {'a': 3,'b': 4}, 'a': {'a': 3,'b': 4}, 'b': {'a': 3,'b': 4},};

def has_duplicates_objects(s):
    d = {}

    for x in s:
        if x in d:
            return True;
        d[x] = True;
    return False;

print(has_duplicates_objects(dictionary));

def rotate_word(word, num):
    new_word = '';
    char = 0;
    for i in word:
        order = ord(i);
        diff = order - num;
        new_word += chr(diff);
    return new_word;

def rotate_pairs(words):
     """Prints all words that can be generated by rotating word.

    word: string
    word_dict: dictionary with words as keys
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)
