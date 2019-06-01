#!/usr/bin/python

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class AvlTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_height(self, node):
        if node is None:
            return 0

        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0

        return self._get_balance(node.left) - self._get_balance(node.right)

    def _rotate_left(self, node):
        return node

    def _rotate_right(self, node):
        return node

    def _insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            self.left = self._insert(root.left, val)
        elif val > root.val:
            self.right = self._insert(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and val < root.left.val:
            return self._rotate_right(root)

        if balance < -1 and val > root.right.val:
            return self._rotate_right(root)

        if balance > 1 and val > root.left.val:
            root.left = self._rotate_left(root.left)
            return self._rotate_left(root.left)

        if balance < 1 and val > root.right.val:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root.left)

    def insert(self, val):
        return self._insert(self.root, val)