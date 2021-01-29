fin = open('words.txt')

def word_scan(file):
    counter_1 = 0;
    counter_2 = 0;
    for line in file:
        counter_1 += 1;
        if len(line.strip()) > 20:
            counter_2 += 1;
            if "e" in line.strip():
                print(line)
    print((counter_2/counter_1)*100)

word_scan(fin);

def avoids(word, letters):
    counter = 0;
    for i in word:
        for c in letters:
            if c in word:
                counter;
    if counter == 0:
        return True;
    return False;

def avoids_modified(word):
    letters = input(': ');
    counter_1 = 0;
    counter_2 = 0;
    for i in word:
        counter_1 = counter_1 + 1;
        for c in letters:
            if c in word:
                counter_2 = counter_2 + 1;
    print(counter_1-counter_2);

def uses_only(word, avail):
    for letter in word:
        if letter not in avail:
            return False;
    return True;

def uses_all_1(word, required):
    for letter in required:
        if letter not in word:
            return False;
    return True;

def uses_all_2(word, required):
    return uses_only(required, word);

abc = 'abcdefghijklmnopqrstuvwxyz';
def is_abecedarian(word):


print(avoids('hello', 'go'));
avoids_modified('hello');

fruit = 'ugk';
print(fruit[:])
