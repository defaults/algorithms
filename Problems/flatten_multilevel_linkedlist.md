**Problem**

Given a linked list where in addition to the next pointer, each node has a child pointer, which may or may not point to a separate list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.You are given the head of the first level of the list. Flatten the list so that all the nodes appear in a single-level linked list. You need to flatten the list in way that all nodes at first level should come first, then nodes of second level, and so on.

*Input:*
1 - 2 - 3 - 4
    |
    7 - 8 - 10 - 12
    |   |    |
    9   16   11
    |   |
    14  17 - 18 - 19 - 20
    |                   |
    15 -23             21
        |
        24

*Output:*
Linked List to be flattened to
1 - 2 - 3 - 4 - 7 - 8 - 10 - 12 - 9 - 16 - 11 - 14 - 17 - 18 - 19 - 20 - 15 - 23 - 21 - 24

**Python Implementation**

```
def flatten_linkedlist(object):

# Node class                                                                                                           
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.child = None

    def create_multilevel_list


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
    pass
```
