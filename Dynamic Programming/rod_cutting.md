 **Problem:**

Gicven a rod of length n and  table of prices Pi for i = 1, 2, 3, ... n, determine the maximum revenue obtanmable by cutting the rod the selling the pieces.

**Reccursive top-down approach**

p is price table eg. p[1, 5, 7, 9, 10, 13....n]
n is length of rod to be cut

Time complexity : O(2⌃n)
```
def cutrod(p,n):
	if n < 0:
		return 0
	else:
		q = -1
		for i in range(0,n + 1):
			q = max(q, p[i] + cutrod(p, n - i - 1 ))

	return q


```
**Dynamic Programming approach:**

*Top-Down with memoization*

Time complexity : O(n⌃2)

```
def memoisedcutrod(p, n):
	r = [-1] * (n+1)
	return topdowncut(p, n, r)

def topdowncut(p, n, r):
	if r[n] >= 0:
		return r[n]
	if n < 0:
		return 0
	else:a
		q = -1
		for i in range(0,n + 1):
			q = max(q, p[i] + topdowncut(p, n - i - 1, r ))

	r[n] = q
	return q

```

*Bottom-Up*

Time complexity : O(n⌃2)

```
def buttomup(p, n):
	r = [0] * (n+1)
	return topdowncut(p, n, r)

	for j in range(0, n + 1):
		q = -1
		for i in range(0, n + 1):
			q = max(q, p[i] + r[j - i - 1])
		r[j] = q

	return r[n]

```
