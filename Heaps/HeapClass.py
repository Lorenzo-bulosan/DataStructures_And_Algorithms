class maxBinaryHeap():
    def __init__(self):
        self.values = []
        self.uniqueValues = {}
        self.length = 0
        
    def __getParentIndex(self, childIndex: int) -> int:
        ''' private helper method to obtain parent index given child index
            In: int index of child in question
            Out: int parent of given child
        '''
        parentIndex = (childIndex-1)//2
        return parentIndex
    
    def __getLeftChildIndex(self, parentIndex: int) -> int:
        ''' private helper method to obtain left child index of a given parent
            In: int index parent in question
            Out: int index of left child of the given parent
        '''
        return (parentIndex*2)+1
    
    def __getRightChildIndex(self, parentIndex: int) -> int:
        ''' private helper method to obtain right child index of a given parent
            In: int index parent in question
            Out: int index of right child of the given parent
        '''
        return (parentIndex*2)+2
    
    def __nodeExist(self, nodeIndex: int) -> list:
        ''' private helper method to find if node exists and return the node
            In: int index of node in question
            Out: [bool, int] denoting if exists or not and the node if it exists
        '''
        try:
            node = self.values[nodeIndex]
            return [True, node]
        
        except: return [False, None]
        
    def peek(self):
        ''' method to observe the node at the root
            In: None
            Out: None
        '''
        return self.values[0]
    
    def heapifyUp(self, node: int, nodeIndex: int):
        ''' method to place the given node to its correct position in the heap
            In: int node value
                int index of given node
            Out: None
        '''
        while(True):
            # compare with parent
            parentIndex = self.__getParentIndex(nodeIndex)
            if(parentIndex < 0): return

            # exit if node in correct position
            parentNode = self.values[parentIndex]
            if(node < parentNode): return
            
            # exchange position in the heap
            self.values[parentIndex] = node
            self.values[nodeIndex] = parentNode
            
            # update node
            nodeIndex = parentIndex
    
    def heapifyDown(self, nodeIndex: int):
        ''' method to move given node to correct position
            In: int index of node in question
            Out: None
        '''
        while(True):
            # get node
            node = self.values[nodeIndex]
            
            # get children positions
            leftNodeIndex = self.__getLeftChildIndex(nodeIndex)
            rightNodeIndex = self.__getRightChildIndex(nodeIndex)
            
            # check if children exists
            [leftExists, leftNode] = self.__nodeExist(leftNodeIndex)
            [rightExists, rightNode] = self.__nodeExist(rightNodeIndex)
            
            # edge case: leaf node
            if(leftExists==False and rightExists==False): return
            
            # edge case: only left child exists
            if(leftExists and rightExists==False):
                if(leftNode > node):
                    self.values[leftNodeIndex] = node
                    self.values[nodeIndex] = leftNode
                return
                
            # both children exists
            elif(leftExists and rightExists):
                if(leftNode > rightNode):
                    self.values[leftNodeIndex] = node
                    self.values[nodeIndex] = leftNode
                    nodeIndex = leftNodeIndex
                else:
                    self.values[rightNodeIndex] = node
                    self.values[nodeIndex] = rightNode
                    nodeIndex = rightNodeIndex
        return

    def insertNode(self, node: int):
        ''' method to insert a node in the correct place in the heap
            In: int value to insert in the heap
            Out: None
        '''
        # edge case: empty heap
        if(self.length == 0):
            self.values.append(node)
            self.uniqueValues[node] = True
            self.length += 1
            return 
        
        # edge case: duplicate value
        if(node in self.uniqueValues): return
        
        # update properties
        self.length += 1
        self.uniqueValues[node] = True
        
        # add to the end
        self.values.append(node)
        nodeIndex = self.length-1
        
        # heapify up
        self.heapifyUp(node, nodeIndex)
        
        return
    
    def removeNode(self, nodeIndex: int) -> int:
        ''' removes node at given index and reorganizes heap
            In: int index of node in question
            Out: int removed node
        '''
        # edge case: empty heap
        if(self.length == 0): return 
        
        # edge case: only 1 element
        if(self.length == 1):
            valueToRemove = self.values.pop()
            self.length -= 1
            self.uniqueValues.pop(valueToRemove)
            return valueToRemove
        
        # get nodes to be swapped
        node = self.values[nodeIndex]
        lastNode = self.values[-1]
        
        # swap nodes
        self.values[nodeIndex] = lastNode
        self.values[-1] = node
        
        # remove nodes and update duplicates list
        valueToReturn = self.values.pop()
        self.uniqueValues.pop(valueToReturn)
        self.length -= 1
        
        # bubble down
        self.heapifyDown(nodeIndex)
        
        return valueToReturn

#%% Test insertNode
print('Testing method: insertNode() --------------')

# testing adding first element and duplicates
heap = maxBinaryHeap()
heap.insertNode(1)
heap.insertNode(1)
if(heap.length == 1): print('Test 1: passed')
else: print('Test 1: failed')
 
# testing heapifying up 1 level
heap = maxBinaryHeap()
heap.insertNode(1)
heap.insertNode(2)
heap.insertNode(6)
if(heap.peek() == 6): print('Test 2: passed')
else: print('Test 2: failed')
 
# testing heapifying up 3 levels
heap = maxBinaryHeap()
for i in [10,1,2,5,7,3]: 
    heap.insertNode(i)
    
if(heap.peek() == 10): print('Test 3: passed')
else: print('Test 3: failed')
 
#%% Testing removeNode
print('\nTesting method: removeNode() --------------')

# testing removing the only element
heap = maxBinaryHeap()
heap.insertNode(1)
largest = heap.removeNode(0)
if(largest==1 and heap.length==0 and len(heap.uniqueValues)==0): print('Test 1: passed')
else: print('Test 1: failed')

# testing removing max in a bigger tree
heap = maxBinaryHeap()
for i in [10,3]: 
    heap.insertNode(i)

removedNode = heap.removeNode(0)
if(removedNode == 10): print('Test 2: passed')
else: print('Test 2: failed')

# testing heapify down edge cases: leaf node
heap = maxBinaryHeap()
for i in [10]: 
    heap.insertNode(i)
    
heap.removeNode(0)
if(heap.values == []): print('Test 3: passed')
else: print('Test 3: failed')

# testing heapify down edge cases: only left child and LARGER than parent
heap = maxBinaryHeap()
for i in [0,7]: 
    heap.insertNode(i)

heap.heapifyDown(0)
if(heap.values == [7,0]): print('Test 4: passed')
else: print('Test 4: failed')

# testing heapify down edge cases: only left child and SMALLER than parent
heap = maxBinaryHeap()
for i in [7,0]: 
    heap.insertNode(i)

heap.heapifyDown(0)
if(heap.values == [7,0]): print('Test 5: passed')
else: print('Test 5: failed')
   
# testing removing max element = root
heap = maxBinaryHeap()
for i in [10,5,9,2,3,6,4]: 
    heap.insertNode(i)

heap.removeNode(0)
if(heap.values == [9,5,6,2,3,4]): print('Test 6: passed')
else: print('Test 6: failed')

# testing inserting with negatives and duplicates and big numbers
heap = maxBinaryHeap()
for i in [-1,2,8,3000,9,9,9,-5000]: 
    heap.insertNode(i)

heap.removeNode(0)
if(heap.values == [9,8,2,-1,-5000]): print('Test 7: passed')
else: print('Test 7: failed')

# testing correct updates of properties
heap = maxBinaryHeap()
for i in [10,5,5,2,3,-1]: 
    heap.insertNode(i)

heap.removeNode(0)
heap.removeNode(0)
if(heap.length == 3 and \
   heap.uniqueValues == {3:True, 2:True, -1:True}): print('Test 8: passed')
else: print('Test 8: failed')





