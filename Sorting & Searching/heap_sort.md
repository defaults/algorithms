**Heap sort** is an efficient sorting algorithm implemented with the heap data structure.

Time complexity:
        Best : O(n log(n))
        Average : O(n log(n))
        Worst : O(n log(n))

Space complexity: O(1)

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
        A[i, A] = A[x]


```

**C++ Implementation**

```
# include <iostream>
using namespace std;

function max_heapify(arr, n, i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if left < n && largest < arr[left]
        largest = arr[left];
        
    if right < n && largest < arr[right]
        largest = arr[right];
        
    if (lagest != i)
    {
        swap(arr[largest], arr[i])
        max_heapify(arr, n, largest);
    }
}

function heap_sort(arr, n):
{
    //build heap
    for(int i = n/2 - 1; i >= 0, i++)
    {
        max_heapify(arr, n, i);
    }
    
    for(int i = n-1, i > 0, i ++)
    {
        swap(arr[0], arr[i];
        max_heapify(arr, i, 0);
    }
}

int main()
{
    int arr[] = [34,34,43,43,33,36,23];
    int n = sizeof(arr[n])/sizeof(arr[0])
    
    heap_sort(arr, n);
}

```


**Javascript Implementation:**

```
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

```
