# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.header, self.trailer = Node(None), Node(None)
        self.header.next, self.trailer.prev = self.trailer, self.header
        self.size = 0

    def len(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.next, nodeToInsert.prev = node, node.prev
        node.prev = nodeToInsert 

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.next, nodeToInsert.prev = node.next, node
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass