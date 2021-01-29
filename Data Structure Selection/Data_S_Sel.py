import string
import requests
import random

#emma = "http://thinkpython2.com/code/emma.txt"

#response = requests.get(emma)

"""
    w = open("words.txt", 'r')

    for q in w.readlines():
        print(q)
"""

file_path = "emma.txt"

"""
for line in file.readlines():
    print(line)
"""

def process_file(file_path):
    hist = dict()
    file = open(file_path, "r")
    #txt = url_file.text;
    for line in file.readlines():
        process_line(line, hist)
    return hist;

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def arr_histogram(array):
    hist = {}
    for word in array:
        hist[word] = hist.get(word, 0) + 1
        hist.get(word, 0)
    return hist;

hist = process_file(file_path)
#print(hist)

def subtract(d1, d2):
    res = dict();
    for key in d1:
        if key not in d2:
            res[key] = None;
    return res

def set_substr(d1, d2):
    return set(d1) - set(d2)

def total_n_words(histogram):
    return sum(histogram.values())

def different_words(hist):
    return len(hist)

def most_frequent_words(hist):
    arr = []
    f_arr = []

    for key, value in hist.items():
        arr.append((value, key))

    arr.sort(reverse=True)

    for i, key in arr[:10]:
        f_arr.append((key, i))

    return f_arr


t = ['a', 'a', 'b']
hist = arr_histogram(t)

def choose_from_hist(hist):
    arr = []

    for i,key in enumerate(hist):
        arr.append(key)

    index = random.randint(0, i)

    return arr[index];

#print(choose_from_hist(hist));

#print(most_frequent_words(hist));

def cum_sum_words(hist):

    w = []
    r = 0

    for q in hist.values():
        r += q
        w.append(r)
    return w

def all_words(hist):

    w = []

    for q in hist.keys():
        print(q)
        w.append(q)
    return w

freqs = cum_sum_words(hist)
print(freqs)
words = all_words(hist)
print(words)

def bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return word_list[i]

    if word_list[i] > word:
        # search the first half
        return bisect(word_list[:i], word)
    else:
        # search the second half
        return bisect(word_list[i+1:], word)

def find_word(sums, words):
    total_freqs = sums[len(sums)-1]
    x = random.randint(0, total_freqs-1)
    index = bisect(words, x)
    return words[index]

book_words = process_file("emma.txt")

def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.

    hist: map from word to frequency
    """
    # TODO: This could be made faster by computing the cumulative
    # frequencies once and reusing them.

    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]



#print(get_words(hist));
