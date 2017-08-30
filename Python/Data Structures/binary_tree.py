#!/usr/bin/python

class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None
		
class BinaryTree:
	def __init__(self):
		self.root = None

	def _height(node):
		if node == None:
			return 0

		return max(height(node.left), height(node.right)) + 1
		
	def _search(self, root, value):
		if root.val == value:
			return root
			
		else:
			return self._search(root.left, value)
			return self._search(root.right, value)
		
	def find_element(self, value):
		if self.root == None:
			return
		
		return self._search(self, self.root, value)
		
	def inorder_traversal(self, root):
		if root == None:
			return
		self.inorder_traversal(root.left)
		print root.val
		self.inorder_traversal(root.right)

	def inorder_traversal_iterative(self, root):
		pass
		
	def preorder_travarsal(self, root):
		if root == None:
			return

		print root.val
		self.inorder_traversal(root.left)
		self.inorder_traversal(root.right)

	def preorder_travarsal_iterative(self, root):
		pass
		
	def postorder_travarsal(self, root):
		if root == None:
			return

		self.inorder_traversal(root.left)
		self.inorder_traversal(root.right)
		print root.val

	def postorder_travarsal_iterative(self, root):
		pass
		
	def levelorder_travarsal(self, root):
		h = height(root)
		for i in xrange(h):
			self._print_level(root, i)

	def _print_level(self, node, level):
		if node == None:
			return

		if level == 0:
			print node.data
		elif level > 0:
			self.print_level(node.left, level - 1)
			self.print_level(node.right, level - 1)

	def levelorder_travarsal_iterative(self, root):
		pass
