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

    # update a node at any index
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present in the linkedlist")
        
    # remove the first node of the linkedlist
    def remove_first_node(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    # remove the last node of the linkedlist
    def remove_last_node(self):
        if self.head is None:
            return
        
        # if there is only one node in the linkedlist
        if self.head.next is None:
            self.head = None
            return
        # transverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # remove a node at any index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")
        