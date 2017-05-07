**Python Implementation:**
```
class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None
		
class BinarySearchTree:
	def __init__(self):
		self.root = None

	def search(self, value):
		if self.root == None:
			return
		
		return self._search(self.root, value)


	def _search(self, root, value):
		if root.data == value:
			return root
		elif root.data > value:
			self._search(root.left, value)

		return self._search(root.right, value)

	def insert(self, value):
		new_node = Node(value)
		if self.root == None:
			self.root = new_node
		else:
			node = self.root

			while node and node.val != value:
				parent = node
				if node.val > value:
					node = node.left

				elif node.val < value:
					node = node.right

			if parent.val > value:
				parent.left = new_node
			else:
				parent.right = new_node

		return

	def delete(self, value):
		if self.root is None:
			return

		self._delete(self.root, value)


	def _delete(self, root, value):
		if root is None:
			return

		if root.val < value:
			self._delete(root.right, value)
		elif root.val > value:
			self._delete(root.left, value)
		else:      # case when value matches
			# case when root has one or no child
			if root.left is None:
				temp = root.right
				root.right = None
				return temp

			elif root.right is None:
				temp = root.left
				root.left = None
				return temp

			# case when root has two children
			temp = min_successor(root.right)

			root.val = temp.val

			root.right = self._delete(root.right, temp.val)

	def _inorder(self, root):
		if root == None:
			return

		self._inorder(root.left)
		print(root.val)
		self._inorder(root.right)

	def inorder(self):
		self._inorder(self.root)



tree = BinarySearchTree()
tree.insert(50)
tree.insert(55)
tree.insert(56)
tree.insert(46)
tree.inorder()
tree.delete(55)
print '\n'
tree.inorder()
```
