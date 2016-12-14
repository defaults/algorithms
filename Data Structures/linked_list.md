**LinkedList**

Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at contiguous location; the elements are linked using pointers.

+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  |  o-------->|  3 | null |
+----+------+     +----+------+     +----+------+

*Python Implementation:*

```
# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

# Creating a simple LinkedList

# Start with the empty list
llist = LinkedList()

llist.head  = Node(1)
second = Node(2)
third  = Node(3)

llist.head.next = second; # Link first node with second

second.next = third;
```

*C++ Implementation:*

```
// A linked list node
struct node
{
  int data;
  struct node *next;
};
```
