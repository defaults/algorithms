#!/usr/bin/python

# Implementation of min heap
class MinHeap:
	def __init__(self):
		self.heap = []
		if not self.size:
			self.size = len(heap)

	# get index of node's parent
	def parent(node):
		return (i - 1) / 2

	# get index of left child
	def left_child(node):
		return 2 * i + 1

	# get index of right child
	def right_child(node):
		return 2 * node + 2

	# extract min from min heap
	def extract_min(self):
		if self.size == 1:
			self.size -= 1
			return heap[0]

		root = self.heap[0]
		self.heap[0], self.heap[size - 1] = self.heap[size - 1], self.heap[0]
		size -= 1
		self.min_heapify()

		return root

	# min heapify
	def min_heapify(self, i):
		smallest = i
		left = left_child(i)
		right = right_child(i)

		if  left < self.size and self.heap[smallest] > heap[left]:
			smallest = heap[left]

		if right < self.size and self.heap[smallest] > heap[right]:
			smallest = heap[right]

		if smallest is not i:
			self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
			# calling min heapify method recursively
			min_heapify(smallest)


# max heap is same logic as above, just have methods like max_heapify and extract_max which are logiacally same but doing opposite thing

