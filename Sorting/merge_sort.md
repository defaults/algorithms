**Merge sort algorithm** follows the **divide-and-cinquer** paradigm. It operates as follows:

**Divide:** Divide the n-element sequence to be sorted into two subsequences of n/2 elements each.

**Conquer:** Sort the sequence recursively using merge sort.

**Combine:** Combine the two sorted subsequences to produce the answer.


**Sudo Code:**

MERGE(A, p, q ,r) // Here A is an array, p,q & r are the indices into the array such that p <= q < r.
n1 = q - p + 1
n2 = r - q
let L[1...n1 + 1] and R[1...n2 + 1] be new arrarys
for i = 1 to n1
    L[i] = A[p + i - 1]
for j = 1 to n2
    R[j] = A[q + j]
L[n1 + 1] = // Sentinel value to mark the end of the array
R[n2 + 1] =
i = 1
j = 1
for k = p to r
    if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
    else A[k] = R[j]
        j = j + 1



MERGE-SORT(A, p, r)
if p < r
    q = [(p + r) / 2]
    MERGE-SORT(A, p, q)
    MERGE-SORT(A, q+1, r)
    MERGE(A, p, q, r)


Python Implementation:
```


```


Javascript Implementation:
