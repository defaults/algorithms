"""
Bucket Sort assumes that the input is drawn from a uniform distribution and has an average-case running time of O(n).

This code assumes that the input is a n element array A and that each element A[i] in the array satisfies 0 <= A[i] < 1.
The code requires and auxiliary array B[0...n-1] of linked list (buckets) and assumens that there is a mahanism for maintaining hat list.

Time complexity:
        Best : O(n + k)
        Average : O(n + k)
        Worst : O(n^2)

Space complexity: O(n)

Psudo code:

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

"""

def  bucketsort(A):
    n = len(A)
    buckets = [[] for i in xrange(n)]

    for i in range(n):
        bi = n * A[i]
        buckets[int(bi)].append(A[i])

    for i in xrange(n):
        buckets[i].sort()

    index = 0
    for i in xrange(n):
        for j in xrange(len(buckets[i])):
            A[index] = buckets[i][j]
            index += 1
    print buckets
    return A

print bucketsort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])

