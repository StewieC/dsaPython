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
