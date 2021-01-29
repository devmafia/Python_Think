import pickle
import dbm
import os

"""
fout = open("output.txt", "w");
line1 = "This is how I feel!";
fout.write(line1);
fout.close();
"""

pattern_string = "aa\r\naah\r\naahed\r\naahing\r\naahs\r\naal\r\naalii\r\naaliis";
rep_string = "hello_bitches";

def sed(pstr, repstr, first_file, second_file):
    """
    1. How to read the first file?
    2. How to write the contents into the second file?
    3. Check, where the string appears in the file?
    4. If we found a match, replace it
    """

    file = open(first_file);
    second_file = open(second_file, "w");
    text = file.read();
    if pattern_string in text:
        print(text);
        text.replace(pattern_string, rep_string);
    second_file.write(text);
    second_file.close();
    file.close();

#sed(pattern_string, rep_string, "words0.txt", "words1.txt");

def finds_anagrams(f):
    d = {};

    file = open(f);

    for line in file:
        word = line.strip().lower();

        t = list(word)
        t.sort()
        t = ''.join(t)

        if t not in d:
            #print(d[t]);
            d[t] = [word];
        else:
            d[t].append(word);

    return d;

file = finds_anagrams('basic_anagrams.txt');

#print(file);

def store_anagrams(dict):
    db = dbm.open('anagrams_db/anagrams','c');

    for word, word_list in dict.items():
        db[word] = str(word_list);

    db.close();

store_anagrams(file);

def read_anagrams(dict):
    return;

def list_dirs(dir):
    """
        1. search the directory, than go for subs, recursively; base case is the current directory
        2. check each path for the suffix, if there is a suffix, add it to the list_dirs
    """
    l = [];

    walk(dir);

    return l;

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name);

        if os.path.isfile(path):
            filename, file_extension = os.path.splitext(path);
            if file_extension == ".mp3":
                l.append(path);
        else:
            walk(path);

def find_duplicates(list_p):
    dupls = [];

    for i,key in enumerate(list_p):
        if key[i] == key[i+1];
            dupls.append(key[i]);

    return dupls;

print(list_dirs(os.getcwd()));
