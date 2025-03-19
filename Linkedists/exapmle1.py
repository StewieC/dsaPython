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
    # indexing starts from 0
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while current_node is not None and position +1 != index:
            position += 1
            current_node = current_node.next
        
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
        else:
            print("Index not present in the linkedlist")
    
    # method to add a node at the end of the linkedlist
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node