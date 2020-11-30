class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        '''
        '''
        if(self.length == 0):
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return self
        
        if(self.length == 1):
            self.length += 1
            self.head = Node(value)
            self.head.next = self.tail
            return self
        
        self.length += 1
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        

        return self