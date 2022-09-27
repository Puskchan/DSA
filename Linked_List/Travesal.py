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
            yield node
            node = node.next
    def insertSL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
                    
    def traverseSL(self):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            while node is not None:
               print(node.value)
               node = node.next


ls = Sll()
ls.insertSL(1,1)
ls.insertSL(2,1)
ls.insertSL(3,2)
ls.insertSL(4,3)
ls.insertSL(0,3)
ls.insertSL(5,-1)
print([node.value for node in ls])
ls.traverseSL()
 



