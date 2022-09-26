class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


ls = Sll()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

ls.head = node1
node1.next = node2
node2.next = node3
ls.tail = node3

ls.__iter__()
