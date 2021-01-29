
str = "There is some code";

def most_frequent(str):
    return;

"""
 1. loop over the list
 2. take each letter and
 3.
"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d;

def most_frequent_2(s):
    l = histogram(str);
    t = [];

    total_freq = 0;
    for i in l:
        total_freq += l[i];
        print(i);
    print(l.values());

f = [5,6,7,8,9]
t = []
"""
for freq, x in f:
    t.append(x);
"""
def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res

#print(most_frequent(str));

file = open("words.txt");

def finds_anagrams(f):
    d = {};

    for line in f:
        word = line.strip().lower();

        t = list(word);
        t.sort();
        t = ''.join(t);

        if t not in d:
            #print(d[t]);
            d[t] = [word];
        else:
            d[t].append(word);

    return d;

anagrams_dict = finds_anagrams(file);
#print(anagrams_dict);

def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)

def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res

#print(print_anagram_sets_in_order(anagrams_dict));
#print(print_anagram_sets_in_order(filter_length(anagrams_dict, 8)));

def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.

    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)
    return d;

def word_distance(word1, word2):
    """Computes the number of differences between two words.

    word1, word2: strings

    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count;

metathesis_pairs(anagrams_dict);
