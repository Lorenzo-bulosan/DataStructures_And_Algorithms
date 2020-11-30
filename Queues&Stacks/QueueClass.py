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
        ''' method to "append" at the end of a list
            In: value of new node to append
            Out: new queue
        '''
        if(self.length == 0):
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return self
        
        if(self.length == 1):
            self.length += 1
            self.tail = Node(value)
            self.head.next = self.tail
            return self
        
        self.length += 1
        elementToInsert = Node(value)
        self.tail.next = elementToInsert
        self.tail = elementToInsert
        return self
    
    def dequeue(self):
        ''' method to remove first element of a queue
            In: None
            Out: first element of the queue
        '''
        if(self.length == 0): return None
        
        if(self.length == 1):
            self.length -= 1
            elementToReturn = self.head
            self.head == None
            self.tail == None
            return elementToReturn
        
        self.length -= 1
        elementToReturn = self.head
        self.head = self.head.next
        return elementToReturn

#%% Testing Queue
import copy

testQueue = Queue()

for i in [9,-12,4,700, 2]:
    testQueue.enqueue(i)

test1 = copy.deepcopy(testQueue)
while(test1.head):
    print(test1.head.value)
    test1.head = test1.head.next

#%% Testing Dequeue
test2 = copy.deepcopy(testQueue)
print('element removed:',test2.dequeue().value,', current length:',test2.length)
print('element removed:',test2.dequeue().value,', current length:',test2.length)
print('element removed:',test2.dequeue().value,', current length:',test2.length)
print('element removed:',test2.dequeue().value,', current length:',test2.length)