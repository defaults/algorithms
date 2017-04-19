"""
The Interpolation Search is an improvement over Binary Search for instances,
where the values in a sorted array are uniformly distributed.
Binary Search always goes to middle element to check.
On the other hand interpolation search may go to different locations according the value of key being searched.
"""

# arr - sorted array, n - item to be sorted
def interpolation_sort(arr, x):
	n = len(arr)
	lo = 0
	hi = n - 1
		
	while arr[lo] <= arr[hi] and x >= arr[lo] and x <= arr[hi]:
		# any one of the can be used
		pivot = lo + (((hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]))
		pivot = lo + ((x - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))
		
		if x == arr[pivot]:
			return pivot
		
		if x < arr[pivot]:
			hi = pivot - 1
		
		else:
			lo = pivot + 1

	if x == arr[lo]:
		return lo
	else:
		return -1
			

arr = [54,64,72,75,80,95,104,111,222]

x = 111

print (interpolation_sort(arr, x))