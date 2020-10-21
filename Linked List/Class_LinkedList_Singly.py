# -*- coding: utf-8 -*-
"""
Singly Linked List Class

"""

class Node:
    
    def __init__(self, val):
        
        self.value = val
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        
        self.length = 0
        self.head = None
        self.tail = None
        
        
    def printAll(self):
        """" Prints all values of the linked list """
        current = self.head
        
        while(current):
            print(current.value)
            current = current.next
            
    def push(self, val):
        """" Inserts value at the end of the list """
        
        node = Node(val)
        
        # edge case: empy list
        if (self.length < 1 ):  
            self.head = node
            self.tail = node
            self.length += 1
            
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
        
        return self
 
    def pop(self):
        """ Removes last node in the list"""
       
        # edge case: empy list
        if (self.length < 1):
            return 'Empty list'
             
        else:
        
            previous = self.head
            current = self.head
            
            while(current.next):
                previous = current
                current = current.next   

            self.tail = previous
            self.tail.next = None
            self.length -= 1
            
            # edge case: single node on list
            if(self.length == 0):
                
                self.head = None
                self.tail = None
                
            return current
    
    def shiftRight(self):
        """ Insterts value at beginning of list """
        
        if (self.length == 0):
            return "Empty list"
        
        current = self.head
        self.head = current.next
        self.length -= 1
        
        if (self.length == 0):
            self.head = None
            self.tail = None
        
        return current
    
    def insertAtBeginning(self, val):
        """Inserts new node at beginning of list"""
        
        if (self.length == 0):
            return "Empty list"
        
        newNode = Node(val)
        current = self.head
        self.head = newNode
        newNode.next = current
        
        self.length += 1
        
        return newNode
        
            

#%% Testing the class
testList = SinglyLinkedList()

for i in range(0,5):
    testList.push(i)
    
#%%
# test print all
testList.printAll() 
print('Length of list: ' + str(testList.length))

# test pop()
#toRemove = testList.pop()
#print('Removed value: ' + str(toRemove.value))

# test shift
removed = testList.shiftRight()
print('Removed value: ' + str(removed.value))

# test insertAtBeginning
#nodeInserted = testList.insertAtBeginning(7)
#print('Inserted value: ' + str(nodeInserted.value))

testList.printAll() 
print('Length of list: ' + str(testList.length))
