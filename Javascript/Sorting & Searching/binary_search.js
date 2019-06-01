function binary_search(A, t) {
	var low = 0;
	var high = A.length - 1;
	while (low <= high) {
		mid = (low + high) / 2;
		if (A[mid] == t) {
			return 'found at :' + mid;
		} else if (A[mid] > t) {
			high = mid - 1;
		}else {
			low = mid + 1;
		}
	}
	return False;
}