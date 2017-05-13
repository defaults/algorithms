**Problem Statement:**
 Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.

 **Python Implementation:**
 *Memoization:*

 ```
 def lcs(a, b, l, m):    # a and b are two arrays and l and m are there respective lengths.
    if l == 0 or m == 0:
        return 0

    if a[l - 1] == b[m - 1]:
        return 1 + lcs(a, b, l - 1, m- 1)
    else:
    return max(lcs(a, b, l - 1, m), lcs(a, b, l, m - 1)))

 ```
