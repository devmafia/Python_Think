import matplotlib
import math
import string
import random
import matplotlib.pyplot as plt
from scipy import special
import numpy as np

# f = cr^-s
# log f = log c = s log r

file_path = "emma.txt"

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

def most_frequent_words(hist):
    arr = []
    f_arr = []

    for key, value in hist.items():
        arr.append((key, value))
        # arr.append([value, key, math.log(value, 10), math.log(key, 10)])

    arr.sort(reverse=True)

    for i, key in enumerate(arr[:10]):
        f_arr.append(key)

    return f_arr

def zipfs_law(file_hist):

    counts = file_hist.values()
    tokens = file_hist.keys()

    #Convert counts of values to numpy array
    s = np.array(counts)

    #define zipf distribution parameter. Has to be >1
    a = 2

    # Display the histogram of the samples,
    #along with the probability density function
    count, bins, ignored = plt.hist(s, 50, normed=True)
    plt.title("Zipf plot for Combined Article Paragraphs")
    x = np.arange(1., 50.)
    plt.xlabel("Frequency Rank of Token")
    y = x**(-a) / special.zetac(a)
    plt.ylabel("Absolute Frequency of Token")
    plt.plot(x, y/max(y), linewidth=2, color='r')
    plt.show()

print(zipfs_law(hist))
