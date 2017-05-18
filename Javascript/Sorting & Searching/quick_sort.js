/*
Quick sort algorithm follows the divide-and-cinquer paradigm.

Algorithmic Paradigm: Divide and Conquer

Time complexity:
        Best : O(n log(n))
        Average : O(n log(n))
        Worst : O(n^2)

Space complexity: O(log(n))

Psudo Code:

Quicksort(A, p, r)
    if p < r
    q = partition(A, p , r)
    quick(A, p, q - 1)
    quick(A, q + 1, r)

partition(A, p , r)
	x = A[r]
	i = p - 1
	for j = p to r - 1
		if A[j] <= x
			i = i + 1
			swap a[i] with a[j]
	swap A[i + 1] with A[r]
	return i + 1
*/

function swap(data, i, j) {
	var tmp = data[i];
	data[i] = data[j];
	data[j] = tmp;
}


function quick(A, p, r) {
	if (p < r) {
		q = partition(A, p, r);
		quick(A, p, q - 1);
		quick(A, q + 1, r);
	}
}

function partition(A, p , r) {
	var x = a[r];
	var i = p - 1;
	var j;
	for (j = p, j < r, j++) {
		if (A[j] <= x) {
			i += 1;
			swap(A, i ,j);
		}
	}
	swap(A, i+1, r);
	return i + 1;
}