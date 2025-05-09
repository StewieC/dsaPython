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


""" UPDATIONG A NODE OF A LINKED LIST

"""
# Update node of a linked list
# at given position
def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
        current_node.data = val
    else:
        while(current_node != None and position != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            current_node.data = val
        else:
            print("Index not present")

"""
DELETE NODE IN LINKEDLIST

"""
# REMOVNG A NODE FROM THE BEGINNING OF THE LINKEDLIST
"""
Steps-by-step approach:

Check if the head of the linked list is None. If it is, return as there are no nodes to remove.
Update the head to point to the next node (self.head = self.head.next), effectively removing the first node from the linked list.ist.
"""
def remove_first_node(self):
    if(self.head == None):
        return
    
    self.head = self.head.next

# REMOVE THE LAST NODE FROM THE LINKEDLIST
"""
Step-by-step Approach:

Check if the head of the linked list is None. If it is, return as there are no nodes to remove.
Initialize a current_node with self.head to start from the head of the list.
Traverse the linked list using a while loop that continues until current_node.next is None or current_node.next.next is None. This ensures the loop stops at the second-to-last node.
Once the loop breaks, current_node will be pointing to the second-to-last node.
Set current_node.next to None, effectively removing the last node from the linked list.
"""

def remove_last_node(self):

    if self.head is None:
        return

    curr_node = self.head
    while (curr_node.next != None and curr_node.next.next != None):
        curr_node = curr_node.next

    curr_node.next = None

# DELETE A NODE AT A SPECIFIC POSITION IN THE LINKEDLIST
"""
Step-by-step Approach:

If the head is None, simply return as there are no nodes to remove.
Initialize a current_node with self.head and a position with 0.
If the position is equal to the index, call the remove_first_node() method.
If the position is not equal to the index, traverse to the node just before the one to be removed using a while loop.
The loop continues until current_node becomes None or position reaches index – 1.
After the loop:
If current_node or current_node.next is None, it means the index is out of range.
If not, bypass the node to be removed by setting current_node.next to current_node.next.next.


"""

def remove_at_index(self, index):
    if self.head is None:
        return
    
    current_node = self.head
    position = 0

    if index == 0:
        self.remove_first_node()
    else:
        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("Index out of range")
        else:
            current_node.next = current_node.next.next

# DELETE A NODE WITH A GIVEN VALUE FROM THE LINKEDLIST

"""
Step-by-step Approach:

Initialize a current_node with the head of the linked list and run a while loop to traverse the list.
The loop continues until current_node becomes None or the data of the node next to current_node matches the given data.
After the loop:
If current_node is None, it means the node with the given data is not present, so return without making any changes.
If the data next to current_node matches the given data, remove that node by updating current_node.next to current_node.next.next, effectively bypassing the node to be removed.
"""

def remove_node (self, data):
    current_node = self.head

    # check if the head node contains the specified data
    if current_node.data == data:
        self.remove_first_node()
        return
    while current_node is not None and current_node.next.data != data:
        current_node = current_node.next

    if current_node is None:
        return
    else:
        current_node.next = current_node.next.next



# LINKEDLIST TRAVERSAL
"""
Step-by-step Approach:

Initialize a current_node with the head of the linked list.
Use a while loop to traverse the linked list, continuing until current_node becomes None.
In each iteration, print the data of the current_node.
After printing, update current_node to the next node in the list by setting current_node to current_node.next.
"""

def printLL(self):
    current_node = self.head
    while(current_node):
        print(current_node.data)
        current_node = current_node.next

# GET THE LENGTH OF A LINKEDLIST

"""
Step-by-step Approach:

Initialize a size counter with 0.
Check if the head is not None. If the head is None, return 0 as the linked list is empty.
Traverse the linked list using a while loop until current_node becomes None.
In each iteration, increment the size by 1.
Once the loop finishes, return the size, which represents the total number of nodes in the linked list.
"""

def sizeOfLL(self):
    size = 0
    if (self.head):
        current_node = self.head
        while(current_node):
            size = size + 1
            current_node = current_node.next
        return size
    else:
        return 0