**Heap sort** is an efficient sorting algorithm implemented with the heap data structure.

Psudo Code:

```
Heapsort(A as array)
    BuildHeap(A)
    for i = n to 1
        swap(A[1], A[i])
        n = n - 1
        Heapify(A, 1)

BuildHeap(A as array)
    n = elements_in(A)
    for i = floor(n/2) to 1
        Heapify(A,i)

Heapify(A as array, i as int)
    left = 2i
    right = 2i+1

    if (left <= n) and (A[left] > A[i])
        max = left
    else
        max = i

    if (right<=n) and (A[right] > A[max])
        max = right

    if (max != i)
        swap(A[i], A[max])
        Heapify(A, max)

```

**Python Implementation:**

```
def heapsort(A):
    buildheap(A)
    for i in xrange(n,1,-1):
        temp = A[1]
        A[1] = a[i]
        a[i] = temp
        n = n -1
        heapify(A, 1)

def buildheap(A):
    n= len(A)
    for i in xrange(n/2,1,-1)
        heapify(A, i)

def heapify(A, i):
    left = 2i
    right = 2i + 1

    if left <= n and A[left] > a[i]:
         max = left
    else:
        max = i

    if right <= n and A[right] > A[max]:
        max = right

    if max != i:
        A[i] = temp
        a[i] = A[max]
        a[max] = temp
        heapify(A, max)

```

**Javascript Implementation:**

```

```
