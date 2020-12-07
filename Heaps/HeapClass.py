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
    
    def peek(self):
        '''
        '''
        return self.values[0]
    
    def heapifyUp(self, node: int, nodeIndex: int):
        '''
        '''
        while(True):
            # compare with parent
            parentIndex = self.__getParentIndex(nodeIndex)
            print('starting indexes',[nodeIndex,parentIndex])
            if(parentIndex < 0): return 0

            # exit if node in correct position
            parentNode = self.values[parentIndex]
            print('comparing node-parent',[node,parentNode])
            if(node < parentNode): return 1
            
            # exchange position in the heap
            self.values[parentIndex] = node
            self.values[nodeIndex] = parentNode
            print('after swap',self.values)
            
            # update node
            nodeIndex = parentIndex

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

#%% Test insertNode
 
# adding first element and duplicate
heap = maxBinaryHeap()
heap.insertNode(1)
heap.insertNode(1)
if(heap.length == 1): print('Test 1 passed')
else: print('Test 1 failed')
 
# testing heapifying up 1 level
heap = maxBinaryHeap()
heap.insertNode(1)
heap.insertNode(2)
heap.insertNode(6)
if(heap.peek() == 6): print('Test 2 passed')
else: print('Test 2 failed')
 
# testing heapifying up 3 levels
heap = maxBinaryHeap()
for i in [10,1,2,5,7,3]: 
    heap.insertNode(i)
    
if(heap.peek() == 10): print('Test 3 passed')
else: print('Test 3 failed')
 
 
 
 
 
   
