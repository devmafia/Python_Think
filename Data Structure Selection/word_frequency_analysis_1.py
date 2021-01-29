
import string

file = open("S_H_Adventures.txt");

"""
l = []

for line in file:
    q = line.strip();
    q = q.split(" ");

    for i,w in enumerate(q):
        print(type(w));
        for i,c in enumerate(w):
            if c in string.whitespace or c in string.punctuation:
                #del w[i]
                break;
        l.append(''.join(w));
print(l);
"""

def allocate_words(filename):

    l = [];

    for line in filename:
        q = line.strip();
        q = q.split(" ");

        for i,w in enumerate(q):
            for j,c in enumerate(w):
                if c in string.whitespace or c in string.punctuation:
                    w = w[:j] + w[(j+1):]
            if w:
                l.append(''.join(w));

    print(l);

allocate_words(file);

"""
l = []

for line in file:
    q = line.strip();
    q = q.split(" ");

    for i,w in enumerate(q):
        print(w);
        word = ""
        for c in w:
            if not (c in string.whitespace or c in string.punctuation):
               word+=c
        if word:
            l.append(''.join(word));

print(l);
"""
