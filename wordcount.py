# put your code here.
import sys
from collections import Counter


def word_count_in_dict(file_name):
    word_count = {}
    my_file = open(file_name)
    for line in my_file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            word = word.lower()
            word = word.strip("?")
            word = word.strip(".")
            word = word.strip(",")
            word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.iteritems():
        print word, count
    my_file.close()


#word_count_in_dict(sys.argv[1])


def counter_based_dict(file_name):

    my_file = open(file_name)
    huge_line = my_file.read()
    #print huge_line
    c = Counter(huge_line.split())

    print c


counter_based_dict("test.txt")