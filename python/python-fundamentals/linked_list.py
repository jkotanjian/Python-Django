class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        print (self.value)

class SList:
    def __init__(self):
        self.head = None
        self.tail = None        

list=SList()
list.head=SLNode('Alice')
list.head.next=SLNode('Chad')
list.head.next.next=SLNode('Debra')