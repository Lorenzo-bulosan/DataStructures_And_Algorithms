def isTreeSymmetric(t):
     
    def DFSinOrder(current):
        
        if(current.right==None and current.left==None):
            numOfLeaf.append(1)
        
        if(current.left):
            DFSinOrder(current.left)
            
        traversedList.append(current.value)
        
        if(current.right):
            DFSinOrder(current.right)
        
        return numOfLeaf
    
    # create variables
    traversedList = []
    firstHalf = []
    secondHalf = []
    current = t
    numOfLeaf = []
    
    #edge case: empty tree
    if(t==None): return True
    
    # DFS in order and store in variable
    DFSinOrder(current)
    
    #split in half
    mid = (len(traversedList)//2)
    firstHalf = traversedList[0:mid]
    secondHalf = traversedList[mid+1:]
    
    # if symmetric 2nd half should be same if reversed*
    if(firstHalf == secondHalf[::-1]):
        if(len(numOfLeaf)%2 == 0): # *even number of leafs
            return True
    
    return False

