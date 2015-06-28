**Merge sort algorithm** follows the **divide-and-cinquer** paradigm. It operates as follows:

**Divide:** Divide the n-element sequence to be sorted into two subsequences of n/2 elements each.

**Conquer:** Sort the sequence recursively using merge sort.

**Combine:** Combine the two sorted subsequences to produce the answer.

Time complexity:
        Best : O(n log(n))
        Average : O(n log(n))
        Worst : O(n log(n))

Space complexity: O(n)

Algorithmic Paradigm: Divide and Conquer

Sorting In Place: No in a typical implementation

Stable: Yes


**Sudo Code:**

MERGE(A, p, q ,r) // Here A is an array, p,q & r are the indices into the array such that p <= q < r.
    n1 = q - p + 1
    n2 = r - q
    let L[1...n1 + 1] and R[1...n2 + 1] be new arrays
    for i = 1 to n1
        L[i] = A[p + i - 1]
    for j = 1 to n2
        R[j] = A[q + j + 1]

    i = 1
    j = 1
    k = p

    while i < n1 and j < n2
        if L[i] <= R[j]
            A[k] = L[i]
            i += 1

        else A[k] = R[j]
            j = j + 1

        k = k + 1

    while i < n1
        A[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n2
        A[k] = R[j]
        j = j + 1
        k = k + 1

MERGE-SORT(A, p, r)
if p < r
    q = [(p + r) / 2]
    MERGE-SORT(A, p, q)
    MERGE-SORT(A, q+1, r)
    MERGE(A, p, q, r)


Python Implementation:
```
// Function to merge the two haves A[p..q] and A[q+1..r] of array A[]
def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q

    // create temp arrays
	L = [0]*n1
	R = [0]*n2

    // Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = A[p + i]
	for j in range(0, n2):
		R[j] = A[q + j + 1]

    // Merge the temp arrays back into A[p..r]
	i = 0
	j = 0
	k = p
	while (i < n1) and (j < n2):

		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j = j + 1

		k +=1


    // Copy the remaining elements of L[], if there are any
	while (i < n1):
		A[k] = L[i]
		i +=1
		k += 1

    // Copy the remaining elements of R[], if there are any
	while (j < n2):
		A[k] = R[j]
		j += 1
		k += 1

// p is for left index and r is right index of the sub-array
  of array A[] to be sorted
def mergesort(A, p, r):
	if p < r:
		q = p + (r - p) / 2      // //Same as (l+r)/2, but avoids overflow for large l and h
		mergesort(A, p, q)
		mergesort(A, q+1, r)
		merge(A, p, q, r)

```

**Javascript Implementation:**

```
function merge(A, p, q, r) {
    var i, j ,k;
    var n1 = q - p + 1;
    var n2 = r - 1;

    var L[n1], R[n2];

    for (i = 0; i < n1; i ++) {
        L[i] = A[p + i]
    }
    for (j = 0; j <n2; j ++) {
        R[j] = A[q + j + 1]
    }

    i = 0, j = 0, k = p;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i ++;
        }
        else {
            A[k] = R[j];
            j ++;
        }
        k ++;
    }

    while (i < n1) {
        A[k] = L[i]
        i++;
        k++;
    }
    while (j < n2) {
        A[k] = R[j]
        j++;
        k++;
    }
}


function mergesort(A, p, r) {
    if (p < r) {
		q = p + (r - p) / 2;
		mergesort(A, p, q);
		mergesort(A, q+1, r);
		merge(A, p, q, r);
    }
}

```
