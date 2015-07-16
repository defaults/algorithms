**Problem:**
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

**Python Implementation:**
*Memoization Implementation*

```
def lis(a):
	n = len(a)
	lis = [1 for i in range(n)]
	for i in xrange(1, n):
		for j in xrange(0, i):
			if a[i] > a[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1

	maximun = max(lis)
	return maximun

```
