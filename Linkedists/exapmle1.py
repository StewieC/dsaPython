# create a node class to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a linkedlist class 
class LinkedList:
    def __init__(self):
        self.head = None

    # add a node at the beginning of the linkedlist
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # method to add at any index
    