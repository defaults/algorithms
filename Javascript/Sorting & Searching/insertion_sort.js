/*
Input: A sequence of number (a1, a2,.... an),

Output: A permutation (reordering) (a1',a2',.... an')

Time complexity:
		Best : O(n)
		Average : O(n^2)
		Worst : O(n^2)

Space complexity: O(1)

Sudo code:

for j = 2 to A.length
	key = A[j]
	i = j - 1
	while i > 0 and [i] > key
		A[i + 1] = A[i]
		i = i - 1
	A[i + 1] = key
*/

function insertionsort)(A) {
	var x = A.length;
	for(var j = 1; j < x; j++) {
		var key = A[j];
		var i = j + 1;
		while(i > -1 && A[i] > key) {
			A[i + 1] = A[i];
			i = i - 1;
		}
		A[i + 1] = key;
	}
}