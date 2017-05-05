*Binary Tree*

**Python Implementation**
```
class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None
		
class BinaryTree:
	def __init__(self):
		self.root = None
		
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
		
	def preorder_travarsal(self):
		if root == None:
			return

		print root.val
		self.inorder_traversal(root.left)
		self.inorder_traversal(root.right)
		
	def postorder_travarsal(self):
		if root == None:
			return

		self.inorder_traversal(root.left)
		self.inorder_traversal(root.right)
		print root.val
		
	def levelorder_travarsal(self):
		if root == None:
			return
		print root.val
		self.inorder_traversal(root.left)
		self.inorder_traversal(root.right)
```