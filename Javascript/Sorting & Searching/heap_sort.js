/*
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
*/

function swap(data, i, j) {
	var tmp = data[i];
	data[i] = data[j];
	data[j] = tmp;
}

 function heap_sort(a) {
	var end = a.length - 1;
	heap_order(a, end);
	while(end > 0) {
		swap(a, 0, end);
		end -= 1
		heapify(a, 0, end);

	}
}

function heap_order(a, end) {
	var i;
	i = end / 2;
	i = Math.floor(i);
	while (i >= 0) {
		heapify(arr, i, end);
		i -= 1;
	}
}

function heapify(a, i, j) {
	var left = 2*i + 1;
	var right = left + 1;
	var max;

	if (left <= j) && (A[left] > A[i]) {
		 max = left;
	}
	else {
		max = i;
	}

	if (right <= j) && (A[right] > A[max]) {
		max = right;
	}

	if (max != i) {
		swap(a, max, i);
		heapify(A, max, j);
	}
}