
**Psudo Code:**

```
Quicksort(A, p, r)
    if p < r
    q = partition(A, p , r)
    quick(A, p, q - 1)
    quick(A, q + 1, r)

partition(A, p , r)
	x = A[r]
	i = p - 1
	for j = p to r - 1
		if A[j] <= x
			i = i + 1
			swap a[i] with a[j]
	swap A[i + 1] with A[r]
	return i + 1
```

**Python Implementation:**

```
def quick(A, p , r):
	if p < r:
		q = partition(A, p , r)
		quick(A, p, q - 1)
		quick(A, q + 1, r)

def partition(A, p , r):
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[i + 1], A[r] = A[r], A[i + 1]
	return i + 1

```

**Javascript Implementation:**

```

function swap(data, i, j) {
    var tmp = data[i];
    data[i] = data[j];
    data[j] = tmp;
}


function quick(A, p, r) {
    if (p < r) {
        q = partition(A, p, r);
        quick(A, p, q - 1);
		quick(A, q + 1, r);
    }
}

def partition(A, p , r) {
    var x = a[r];
    var i = p - 1;
    var j;
    for (j = p, j < r, j++) {
        if (A[j] <= x) {
            i += 1;
            swap(A, i ,j);
        }
    }
    swap(A, i+1, r);
    return i + 1;
}

```
