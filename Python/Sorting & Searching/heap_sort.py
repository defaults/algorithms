"""
Heap sort is an efficient sorting algorithm implemented with the heap data structure.

Time complexity:
        Best : O(n log(n))
        Average : O(n log(n))
        Worst : O(n log(n))

Space complexity: O(1)

Psudo Code:

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
"""

def heapsort(A):
	j = len(A) - 1
	buildheap(A, j)

	for i in range(j,0,-1):
		A[0], A[i] = A[i], A[0]
		j -= 1
		heapify(A, 0, j)

	print A

def buildheap(A, j):
	for i in range(j/2,-1,-1):
		heapify(A, i, j)

def heapify(A, i, j):
	left = 2*i + 1
	right = left + 1

	if left <= j and A[left] > A[i]:
		 max = left
	else:
		max = i

	if right <= j and A[right] > A[max]:
		max = right

	if max != i:
		A[i], A[max] = A[max], A[i]
		heapify(A, max, j)

        
a = [3,2,5,7,12,76,33,21]
heapsort(a)
