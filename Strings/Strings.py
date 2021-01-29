# 8.2
a = 'banana'.count('a');
print(a);

# 8.3
def is_polindrome(word):
    return word[0::1] == word[::-1];

print(is_polindrome('woo'));

# 8.5
def rotate_word(word, num):
    new_word = '';
    char = 0;
    for i in word:
        order = ord(i);
        diff = order - num;
        new_word += chr(diff);
    return new_word;

print(rotate_word('hello', 5));
