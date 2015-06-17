**Counting Sort** assumes that each of the n input elements in a integer in the range 0 to k for some integer k. When k = O(n) time.

**Psudo Code**

```
Counting-Sort(A, B, k):
    let C[0...k] be a new array
    C[i] = 0
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1

    // C[i] now contains the number of elements equal to i.

    for i = 1 to k
        C[i] = C[i] + C[i - 1]

    // C[i] now contains the number of elements less than or equal to i.

    for j = A.length to 1
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
```

**Python Implementation:**

```
def countingsort(A, B, k):
    C = [0]
    n = len(A)
    for j in range(0,n):
        c[A[j]] += 1

    for i in range(0, k):
        C[i] = C[i] + C[i - 1]

    for j in range(n,0):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    return A
```

**Javascript Implementation:**

```
function countingsort(A, B, k) {
    var C = [0];
    var n = len(A);
    for (int j = 0; j < n; j++) {
        c[A[j]] += 1;
    }

    for (int i = 0; i < k; i ++) {
        C[i] = C[i] + C[i - 1];
    }

    for (int j = n; j < 0; j--) {
        B[C[A[j]]] = A[j];
        C[A[j]] = C[A[j]] - 1;
    }
    return A;
}

```
