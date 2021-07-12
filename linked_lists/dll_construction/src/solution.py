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
        self.size += 1

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.next, nodeToInsert.prev = node.next, node
        node.next = nodeToInsert
        self.size += 1

    def insertAtPosition(self, position, nodeToInsert):
        node = self.header
        for i in range(position + 1):
            node = node.next

        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.header
        for i in range(self.size):
            node = node.next
            if node.value == value:
                self.remove(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None
        self.size -= 1

    def containsNodeWithValue(self, value):
        node = self.header
        for i in range(self.size):
            node = node.next
            if node.value == value:
                return i
        return False
