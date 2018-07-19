#!/usr/bin/python
"""
Binary Indexred Tree
"""

class BinaryIndexedTree(object):
    def __init__(self, length=0):
        self.bit = [0 for i in range(length + 1)]
        self.length = length

    def get_sum(self, index):

        # BIT has one extra index than the array
        index += 1
        sum_till_index = 0

        while index > 0:
            sum_till_index += self.bit[index]
            index -= index & (-index)

        return sum_till_index

    def update(self, index, val):
        index += 1

        while index <= self.length:
            self.bit[index] += val
            index += index & (-index)

        return

    def contruct(self, array):
        length = len(array)

        self.length = length
        self.bit = [0 for i in range(self.length + 1)]

        for index in range(self.length):
            self.update(index, array[index])

        return self.bit


freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit_tree = BinaryIndexedTree()
bit_tree.contruct(freq)

print(bit_tree.get_sum(5))
bit_tree.update(2, 3)
print(bit_tree.get_sum(5))
