"""
MO Algorithm is usefull for problems having queries for subarrays in an array.
Each query is of the form left, right.

MO algorithm does not work with live quries and updating array

E.g. - Let a array A[n], Q[m] havin queries for sum of subarray.

Time Complexity - O( (n + m) * Sqrt(n)) ~ O( n * Sqrt(n))
"""

def query_results(A, Q):
    n = len(A)
    m = len(Q)

    curr_l, curr_r, curr_sum = 0

    for i in xrange(m):
        left = Q[i].L
        right = Q[i].R

        while curr_l <= left:
            curr_sum -= A[curr_l]
            curr_l += 1

        while curr_l > left:
            curr_l += A[curr_l - 1]
            curr_l -= 1

        while curr_r <= right:
            curr_sum += A[curr_r]
            curr_r += 1

        while curr_r > right:
            curr_r -= A[curr_r - 1]
            curr_l -= 1

        print 'sum of %d to %d is %d', (left, right, curr_sum)

    return

