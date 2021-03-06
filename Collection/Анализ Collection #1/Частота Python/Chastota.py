import os
from collections import Counter
import glob

def word_frequency(fileobj, words):
    """Build a Counter of specified words in fileobj"""
    # initialise the counter to 0 for each word
    ct = Counter(dict((w, 0) for w in words))
    file_words = (word for line in fileobj for word in line.split())
    filtered_words = (word for word in file_words if word in words)
    return Counter(filtered_words)



def count_words_in_dir(dirpath, words, action=None):
    """For each .txt file in a dir, count the specified words"""
    for filepath in glob.iglob(os.path.join(dirpath, '02.txt')):
        with open(filepath) as f:
            ct = word_frequency(f, words)
            if action:
                action(filepath, ct)


def print_summary(filepath, ct):
    f04 = open('Output.txt', 'w')
    words = sorted(ct.keys())
    counts = [str(ct[k]) for k in words]
    f04.write('{0}\n{1}\n{2}\n\n'.format(
        filepath,
        ', '.join(words),
        ', '.join(counts)))



Ynik = open('Словарь.txt', 'r')
words = [line.strip() for line in Ynik]


count_words_in_dir('./', '1' , action=print_summary)


