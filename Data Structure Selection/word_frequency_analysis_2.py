import string

file = open("S_H_Adventures.txt");

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

    return l;

def read_the_book(filename):

    for line in filename:
        print(line.strip());

read_the_book(file);
