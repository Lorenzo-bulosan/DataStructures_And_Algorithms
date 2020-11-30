
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.length = 0
        self.head = None
    
    def push(self, value):
        ''' method to add a new node at the start of the stack
            In: value of new node to insert
            Out: stack of nodes
        '''
        
        if(self.length == 0):
            self.length += 1
            self.head = Node(value)
            self.head.next = None
            return self
        
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
        
        return self

    def pop(self):
        ''' method to remove the first element from stack
        '''
        if(self.length == 0): return None
        
        if(self.length == 1):
            self.length -= 1
            elementToReturn = self.head
            self.head = None
            return elementToReturn
        
        else:
            self.length -= 1
            elementToReturn = self.head
            self.head = self.head.next
            
            return elementToReturn
    
#%% Testing the stack push
import copy
testStack = Stack()

for i in [5,-2,300,4]:
    testStack.push(i)

stackTest1 = copy.deepcopy(testStack)
while(stackTest1.head):
    print('stack element:',stackTest1.head.value)
    stackTest1.head = stackTest1.head.next

print('current length of stack:',stackTest1.length)

#%% Testing stack pop
stackTest2 = copy.deepcopy(testStack)

print('pop:',stackTest2.pop().value,', new lenght',stackTest2.length)
print('pop:',stackTest2.pop().value,', new lenght',stackTest2.length)

