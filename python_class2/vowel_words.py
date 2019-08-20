
""" In Repl:
file_reader = open('dictionary.txt', encoding='utf-8')
line = file_reader.readline()
line
line.strip()

for line in file_reader:
    line = line.strip()
    print(line)
    if line == 'abalones':
        break


file_reader.close()
file_reader = open('dictionary.txt')
"""

def has_upper(word):
    return any(letter.isupper() for letter in word)

def starts_with_vowel(word):
    return word[0].lower() in 'aeiou'

def has_no_e(word):
    return 'e' not in word.lower()

def only_one_vowel(word):
    vowels = {
        letter.lower()
        for letter in word
        if letter.lower() in 'aeiou'
    }
    return len(vowels) == 1

def has_5_vowels(word):
    vowels = {
        letter.lower()
        for letter in word
        if letter.lower() in 'aeiou'
    }
    return len(vowels) == 5


count = 0
for line in file_reader:
    line = line.strip()
    if has_5_vowels(line):
        print(line)
        count += 1
    if count == 10:
        break

def count_words(file_name, func):
    count = 0
    file_handle = open(file_name)
    for word in file_handle:
        word = word.strip()
        if func(word):
            count += 1
    file_handle.close()
    return count

def silly_case(sentences):
    return sentences.title().swapcase()
