# Given a string, print all permutations of it in sorted order. For example, if the input string is “ABC”, then output should be “ABC, ACB, BAC, BCA, CAB, CBA”.


# Solution
def findceil(a, first, l, h):
    index = l

    for i in range(l + 1, h + 1):
        if a[i] > first and a[i] < a[index]:
            index = i

    return index


def sorting(a, b, size):
    # more efficient sorting(actually reversing) as the subarray we get after swapping is always in reverse order. Overall time complexity O(n x n!) !!!
    while(b < size):
        a[b + 1], a[size - 1] = a[size - 1], a[b + 1]
        b += 1
        size -= 1
    return a

# basic sorting using bubble sort. Overall time complexity O(n^2 x n!)
    # for i in range(b + 1, size):
    #     for j in range(b + 1, size - 1):
    #         if a[j] > a[j + 1]:
    #             a[j], a[j + 1] = a[j + 1], a[j]
    # return a


def laxical(a):
    size = len(a)
    a = sorted(a)

    i = 1
    while(i != -1):
        print (''.join(a))

        for i in xrange(size - 2, -2, -1):
            if a[i] < a[i + 1]:
                break

        if i == -1:
            break

        else:
            index = findceil(a, a[i], i + 1, size - 1)
            a[i], a[index] = a[index], a[i]
            sorting(a, i, size)

x = raw_input()
laxical(x)

for i in range(10):
    print(x)
