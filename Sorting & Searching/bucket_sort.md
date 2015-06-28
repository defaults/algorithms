**Bucket Sort** assumes that the input is drawn from a uniform distribution and has an average-case running time of O(n).

This code assumes that the input is a n element array A and that each element A[i] in the array satisfies 0 <= A[i] < 1.
The code requires and auxiliary array B[0...n-1] of linked list (buckets) and assumens that there is a mahanism for maintaining hat list.

Time complexity:
        Best : O(n + k)
        Average : O(n + k)
        Worst : O(n^2)

Space complexity: O(n)

**Psudo code:**

```
Bucket-Sort(A)
    let B[0...n-1] be a new array
    n = A.length
    for i = 0 to n-1
        make B[i] an empty list
    for i = 1 to n
        insert A[i] into list B[ |nA[i]| ]
    for i = 0 to n-1
        sort list B[i] with insertion sort

    concatenate the list B[0], B[1],...., B[n - 1] together in order.

```

**Python Implementation:**

```
def  bucketsort(A):
    n = len(A)

    for i in range(0, n):


```

**Javascript Implementation:**

```


```
