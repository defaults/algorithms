"""
Redix Sort is preety straight forward. The folowing procedure assumes that each element in the n-element array A has d digits, where 1 is the lowest-order digit and d id the highest order digit.

Time complexity:
        Best : O(nk)
        Average : O(nk)
        Worst : O(nk)

Space complexity: O(n+k)

Psudo Code:

Radix-Sort(A, d)

for i = 1 to d
    use a stable sort to sort array A on digit d.

"""

def countsort(A, n, exp):
	B = [0]*n
	C = [0]*10

	for i in range(0,n):
		C[(A[i]/exp) % 10] += 1

	for i in range(1,10):
		C[i] += C[i - 1]

	for i in range(n-1, -1, -1):
		B[C[ (A[i]/exp) % 10] - 1] = A[i]
		C[ (A[i]/exp) % 10] -= 1

	for i in range(0,n):
		A[i] = B[i]


def redix(A):
	n = len(A)
	mx = max(A)

	for exp in range(0,n):
		countsort(A, n, exp)

	return A
