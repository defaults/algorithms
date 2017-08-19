#!usr/bin/python

"""
A suffix array is a sorted array of all suffixes of a given string.

Advantages of suffix arrays over suffix trees include improved space requirements,
simpler linear time construction algorithms (e.g., compared to Ukkonen algorithm) and
improved cache locality.
"""

# Naive Method for building Suffix Array

# Time Complexity: O(n2Logn)

class Suffix:
    index = 0
    suff = ''

def compare(a, b):
    return cmp(a.suff, b.suff)

def build_suffix_array(text):
    lenght = len(text)

    suffixes = []

    for i in xrange(lenght):
        suffix = Suffix()
        suffix.index = i
        suffix.suff = text[i:]
        suffixes.append(suffix)

    suffixes  = sorted(suffixes, key=lambda i : i.suff)

    suffix_array = []
    for i in xrange(lenght):
        suffix_array.append(suffixes[i].index)

    return suffix_array


text = 'banana'
suffix_array = build_suffix_array(text)
print('Following is the text for suffix array: ', suffix_array)


# Optimized O(nLogn) method to build Suffix Array

# Time Complexity: O(nLogn)

class Suffix:
    index
