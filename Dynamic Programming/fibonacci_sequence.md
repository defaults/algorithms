**Finding nth Finobacci number in O(log n)**


*recursive:*
```
def finobacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return finobacci(n - 1) + finobacci(n - 2)


```
*top down:*

```
def finobacci(n):
    f = [ ] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in xrange(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

```
