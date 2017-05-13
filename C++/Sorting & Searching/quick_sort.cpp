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

#include <iostream>

using namespace std;

void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int partition(int arr[], int lo, int hi)
{
	int pivot = arr[hi];
	int i = lo - 1;
	for(int j=lo; j<hi; j++)
	{
		if(arr[j] <= pivot)
		{
			i += 1;
			 swap(&arr[i], &arr[j]);
		}
			
	}

	swap(&arr[i + 1], &arr[hi]);

	return (i + 1);
}

void quick_sort(int arr[], int lo, int hi)
{
	if(lo < hi)
	{
		int pi = partition(arr, lo, hi);
		
		quick_sort(arr, lo, pi - 1);
		quick_sort(arr, pi + 1, hi);	
	}
}
	
/* Function to print an array */
void printArray(int arr[], int size)
{
	int i;
	for (i=0; i < size; i++)
		printf("%d ", arr[i]);
	printf("\n");
}
	
int main(int argc, char *argv[])
{
	int arr[] = {10, 7, 8, 9, 1, 5};
	int n = sizeof(arr)/sizeof(arr[0]);
	quick_sort(arr, 0, n-1);
	printf("Sorted array: \n");
	printArray(arr, n);
	return 0;
}
