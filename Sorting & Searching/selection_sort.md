Selection sort is a sorting algoritm in which on very loop smallest element is selected and swaped with the first element of the array.

Time complexity = O(n2)
Space Complexity = O(1)

**Python Implementation**

```
def selection_sort(arr, index):
	size = len(arr, index)
	
	min = arr[index]
	for i in xrange(index + 1, size):
		if min > arr[i]:
			min,arr[i] = arr[i], min
			

for i in xrange(len(arr)):
	selection_sort(arr, i)
	
print arr
```
