#!/usr/bin/python

"""
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

The best case occurs when the first character of the pattern is not present in text at all.

	txt[]  = "AABCCAADDEE"
	pat[] = "FAA"

The number of comparisons in best case is O(n).


The worst case of Naive Pattern Searching occurs in following scenarios.

1) When all characters of the text and pattern are same.
	txt[] = "AAAAAAAAAAAAAAAAAA"
	pat[] = "AAAAA"

2) Worst case also occurs when only the last character is different.
	txt[] = "AAAAAAAAAAAAAAAAAB"
	pat[] = "AAAAB"

Number of comparisons in worst case is O(m*(n-m+1))
"""

def search(pattern, text):
	m = len(pattern)
	n = len(text)

	for i in xrange(n - m + 1):
		for j in xrange(m):
			if text[i + j] != pattern[j]:
				break

			if j == m - 1:
				print("Pattern found at index: " + str(i))


txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt)
	