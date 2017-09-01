"""
A Priroty Queue is a data structure for maintaining a set S of elements each with associated valur called a key.
As with heaps, priority queues have two forms - max-priority and min-priority queues.

A Max-Pririty Queue supports the following operations:
Insert(S, x)
Maximun(S)
Extract-Max(S)
Increase-Key(S, x, k)

Psudo Code:

Maximum(A)
    return A[1]

ExtractMax(A)
    if A.size < 1
        error 'heap underflow'
    max = A[1]
    A[1] = A[A.size]
    A.size = A.size - 1
    Heapify(A, 1)                       //same function as heapsort to max heapify, refer heapsort for code.
    return max

IncreaseKey(A, x, k)
    if key < A[i]
        error 'new key is smaller than current key'
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]
        exchange A[i] with A[parent(i)]
        i = parent(i)

Insert(A, key)
    A.size = A.size + 1
    A[A.size] = - @
    IncreaseKey(A, A.size, key)

"""
