# practice file

class Node:
    ''' Creating node class
    consist of only a value and pointing property
    '''
    def __init__(self,val):
        self.value = val
        self.next = None

class singlyLinkedList:
    ''' Creating singly linked list class
    unlike lists they do not have indexes 
    '''
    def __init__(self):
        ''' we only keep track of tail head and length'''
        
        self.head = None
        self.tail = None
        self.length = 0
        
    def printAll(self):
        
        allValues = []
        currentNode = self.head
        
        for i in range(self.length):
            allValues.append(currentNode.value)
            currentNode = currentNode.next
        
        print(allValues)
        return self
    
    def push(self,val):
        newNode = Node(val)
        
        # check if empty
        if(self.length < 1):
            self.head = newNode
            self.tail = newNode
            
        # handle list with existing data
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            
        # update length
        self.length += 1 
        
        return self
    
    def pop(self):
        
        # check if empty
        if(self.length < 1):
            return 'empty list'
        
        elif(self.length == 1):
            self.tail = None
            self.head = None
            self.length -= 1 
        
        else:
            currentNode = self.head
            nextNode = self.head
            
            # traverse the linked list
            for i in range(self.length-1):
                currentNode = nextNode
                nextNode = currentNode.next
            
            print(currentNode.value)
            self.tail = currentNode
            self.tail.next = None
            self.length -= 1
            
            return 
        
    def shiftRight(self):
        
        # check if empty
        if(self.length < 1):
            return 'empty list'
        
        else:
            self.head = self.head.next
            self.length -= 1
            
        
            
                
            
#%% Test push
list1 = singlyLinkedList()

list1.push(5)
print([list1.head.value, list1.tail.value, list1.length])
        
list1.push(7)
print([list1.head.value, list1.tail.value, list1.length])

#%% Test pop
list2 = singlyLinkedList()
length = 8

for i in range(length):
    list2.push(i)

list2.printAll()
list2.pop()
list2.printAll()

#%% Test shiftRight

# create instance
list3 = singlyLinkedList()

# populate test data
length = 8
for i in range(length):
    list3.push(i)

#test
list3.printAll()
list3.shiftRight()
list3.printAll()


