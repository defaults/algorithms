**Input:** A sequence of number (a1, a2,.... an),

**Output:** A permutation (reordering) (a1',a2',.... an')

**Sudo code:**

for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and [i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key


**Python Implementation:**

```
def insertionsort(A):
    x = len(A)
    for j in range(1, x):
    	key = A[j]
    	i = j - 1
    	while i > -1 and A[i] > key:
    		A[i + 1] = A[i]
    		i = i - 1
    	A[i + 1] = key

    return A

```

**Javascript Implementation:**

```
var j = 2;
var x = A.length;
for(; j<=x; j++) {
    var key = A[j];
    var i = j + 1;
    while(i > 0 && A[i] > key) {
        A[i + 1] = A[i];
        i = i - 1;
    }
    A[i + 1] = key;
}

```
