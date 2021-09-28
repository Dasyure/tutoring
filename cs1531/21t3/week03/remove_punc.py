# https://www.geeksforgeeks.org/string-punctuation-in-python/
# https://www.w3schools.com/python/ref_string_split.asp
# https://www.w3schools.com/python/ref_string_strip.asp

import string

with open("tolstoy.txt") as INFILE:
    with open("no_punctuation.txt", "w") as OUTFILE:
        for line in INFILE:
            for word in line.split():
                print(word.strip(string.punctuation), end=' ', file=OUTFILE)
            print(file=OUTFILE)
