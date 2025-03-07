class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # insertion at the begining of the list

    """
    create a new node with the given data,
    check if the head of the linkelist is empty, if yes, set the new node as the head
    else, if no, proceed to the next step
    set the next of the new node to the current head
    make the new node the head of the linkedlist
    return the head of the linkedlist which is the new node

    """
def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node


# INSERT A NODE AT A SPECIFIC POSITION IN LINKEDLIST

"""
Step-by-step Approach:

Create a new_node with the given data, a current_node that is set to the head, and a counter ‘position’ initialized to 0.
If the index is 0, it means the node should be inserted at the beginning, so call the insertAtBegin() method.
If the index is not 0, run a while loop until:
The current_node is not equal to None, or
The position+1 is not equal to the index.
In each iteration, increment the position by 1 and update current_node to its next node.
When the loop breaks:
If current_node is not None, insert the new_node after the current_node.
If current_node is None, it means the index is not present in the list, so print “Index not present”.
"""

# Method to add a node at any index
# Indexing starts from 0.
def insertAtIndex(self, data, index):
    if (index == 0):
        self.insertAtBegin(data)
        return

    position = 0
    current_node = self.head
    while (current_node != None and position+1 != index):
        position = position+1
        current_node = current_node.next

    if current_node != None:
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
    else:
        print("Index not present")


"""
INSERT AT THE END OF THE LIST 

Step-by-step Approach:

Create a new_node with the given data.
Check if the head is an empty node:
If the head is empty, make the new_node the head and return.
If the head is not empty, set current_node to the head.
Traverse the linked list by running a while loop until current_node becomes None, indicating the last node.
Once the loop breaks, insert the new_node after the current_node, which is the last node of the linked list.


"""

def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return

    current_node = self.head
    while(current_node.next):
        current_node = current_node.next

    current_node.next = new_node
