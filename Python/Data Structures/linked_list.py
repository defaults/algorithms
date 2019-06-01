"""
LinkedList

Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at contiguous location; the elements are linked using pointers.

+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  |  o-------->|  3 | null |
+----+------+     +----+------+     +----+------+
"""

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

    def push(self, data):
        new_node = Node(data)
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # Change the next of last node
        last.next =  new_node

    def insert_after(self, pre_node, new_data):
        if pre_node is None:
            print(given previous node must be LinkedList)
            return

        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def delete_node(self, key):
        temp = self.head


        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        if temp == None:
        return

        prev.next = temp.next
        temp = None

    # Given a reference to the head of a list and a position, delete the node at a given position
    def deleteNode(self, position):
        self.head = temp

        if temp == None:
            return

        if position == 0:
            self.head = temp.next
            temp  = None

        for i in xrange(position - 1):
            temp = temp.next
            if temp == None:
                return

        # return in case of previous node or node to be deleted be none
        if temp == None:
            return
        if temp.next == None
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    #reverse a LinkedList
    def reverse_list(self):
        current_node = self.head
        prev_node = None

        while(current_node):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            temp = next_node

        self.head = prev_node

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
    l_list = LinkedList()

    l_list.push(5)
    l_list.push(2)
    l_list.append(6)
    l_list.push(1)

    print 'Printing LinkedList:', l_list.printList()

    # Printing LinkedList: 1 2 5 6
