Input : A sequence of number (a1, a2,.... an),

Output : A permutation (reordering) (a1',a2',.... an')

Sudo code:

for j = 2 to A.length
    key = a[j]
    i = j - 1
    while i > 0 and [i] > key
        A[i + 1] = a[i]
        i = i - 1
        a[i + 1] = key


Python Implementation:

x = len(A)
for j in range(2, x):
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key:
        a[i + 1] = a[i]
        i = i + 1
        a[i + 1] = key

Javascript Implementation:

var j = 2;
var x = A.length;
for(; j<=x; j++) {
    var key = A[j];
    var i = j + 1;
    while(i > 0 && A[i] > key) {
        A[i + 1] = A[i];
        i += 1;
        A[i + 1] = key;
    }
}
