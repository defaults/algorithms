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

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next


# Creating a simple LinkedList
# A simple Python program for traversal of a linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next


# Code execution starts here
if __name__=='__main__':
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
// A simple C program for traversal of a linked list
#include<stdio.h>
#include<stdlib.h>

struct node
{
  int data;
  struct node *next;
};

// This function prints contents of linked list starting from
// the given node
void printList(struct node *n)
{
  while (n != NULL)
  {
     printf(" %d ", n->data);
     n = n->next;
  }
}

int main()
{
  struct node* head = NULL;
  struct node* second = NULL;
  struct node* third = NULL;

  // allocate 3 nodes in the heap
  head  = (struct node*)malloc(sizeof(struct node));
  second = (struct node*)malloc(sizeof(struct node));
  third  = (struct node*)malloc(sizeof(struct node));

//assign data and link
  head->data = 1;
  head->next = second;

  second->data = 2;
  second->next = third;

  third->data = 3;
  third->next = NULL;

  printList(head);

  return 0;
}
```
