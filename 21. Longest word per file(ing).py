import os

def find_longest_word(filename):
    longest_word=''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word)>len(longest_word):
                longest_word=one_word
        return longest_word

def find_all_longest_words(dirname):
    return {filename:find_all_longest_words(os.path.join(dirname,filename))}
    for filename in os.listdir(dirname)
    if os.path.isfile(os.path.join(dirname,filename))