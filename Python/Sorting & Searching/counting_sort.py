"""
Counting Sort assumes that each of the n input elements in a integer in the range 0 to k for some integer k. When k = O(n) time. It is often used as a sub-routine to another sorting algorithm like radix sort.

Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
Auxiliary Space: O(n+k)

Psudo Code

Counting-Sort(A, B, k):
    let C[0...k] be a new array
    C[i] = 0
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1

    // C[i] now contains the number of elements equal to i.

    for i = 1 to k
        C[i] = C[i] + C[i - 1]

    // C[i] now contains the number of elements less than or equal to i.

    for j = A.length to 1
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
"""

def countingsort(A, k):
	n = len(A)
	B = [0]*(n)
	C = [0]*(k+1)

	for j in range(0,n):
		C[A[j]] += 1

	for i in range(1, k+1):
		C[i] += C[i - 1]

	for j in xrange(n-1, -1, -1):
		B[C[A[j]] -  1] = A[j]
		C[A[j]] -= 1

	return B
