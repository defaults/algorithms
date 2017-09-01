"""
Trie is an efficient information retrieval data structure. Using trie, search complexities can be brought to optimal limit (key length). If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. Using trie, we can search the key in O(M) time. However the penalty is on trie storage requirements.

Search: O(M)
Add: 
Delete:

Space Complexity: O(ALPHABET_SIZE * key_length * N) = ~ O(M * N)
"""

class Node:
	def __init__(self):
		self.children = {}
		self.is_leaf = False

	def add_child(self, key, data=None):
		pass


class Trie:
	def __init__(self):
		self.head = self.get_node()

	def get_node(self):
		return Node()

	def _chartoindex(self, char):
		return ord(char) - ord('A')

	def insert(self, word):
		current_node = self.head
		for i in xrange(len(word)):
			index = self._chartoindex(word[i])
			if not current_node.children.has_key(index):
				current_node.children[index] = self.get_node()
			current_node = current_node.children[index]

		current_node.is_leaf = True

	def search(self, word):
		current_node = self.head

		for i in xrange(len(word)):
			index = self._chartoindex(word[i])
			if index not in current_node.children:
				return False
			current_node = current_node.children[index]

		return current_node != None and current_node.is_leaf

	def _delete_helper(self, word, length):
		if root:
			pass
			

	def delete(self, word):
		if len(word) > 0:
			return self._delete_helper(self, word, length)
			
	def get_word_from_node(self, current_node, result, prefix):
		if current_node.is_leaf:
			result.append(prefix)
		else:
			for val, node in current_node.children.items():
				self.get_word_from_node(node, result, prefix + chr(val + ord('A')))


	def start_with_prefix(self, prefix):
		current_node  = self.head

		for i in xrange(len(prefix)):
			index = self._chartoindex(prefix[i])
			if index in current_node.children:
				current_node = current_node.children[index]
			else:
				return None

		print [chr(x + ord('A')) for x in current_node.children.keys()]
		result = []
		
		for val, node in current_node.children.items():
			self.get_word_from_node(node, result, prefix + chr(val + ord('A')))

		print result

if __name__ == "__main__":
	states = """
			Alabama
			Alaska
			Arizona
			Arkansas
			California
			Colorado
			Connecticut
			Delaware
			Florida
			Georgia
			Hawaii
			Idaho
			Illinois
			Indiana
			Iowa
			Kansas
			Kentucky
			Louisiana
			Maine
			Maryland
			Massachusetts
			Michigan
			Minnesota
			Mississippi
			Missouri
			Montana
			Nebraska
			Nevada
			New Hampshire
			New Jersey
			New Mexico
			New York
			North Carolina
			North Dakota
			Ohio
			Oklahoma
			Oregon
			Pennsylvania
			Rhode Island
			South Carolina
			South Dakota
			Tennessee
			Texas
			Utah
			Vermont
			Virginia
			Washington
			West Virginia
			Wisconsin
			Wyoming"""
	states_list = [w.strip().lower() for w in states.splitlines() if w]
	trie = Trie()
	for state in states_list:
		trie.insert(state)
		
	print trie.search('california')
	trie.start_with_prefix('t')