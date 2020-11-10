def kthSmallestInBST(t, k):

    # recursive helper function
    def DFSinOrder(t):
        # check left nodes if they exist 
        if(t.left):
            DFSinOrder(t.left)
            
        # append to list
        listInOrder.append(t.value)
        
        # check right nodes if they exist
        if(t.right):
            DFSinOrder(t.right)   
        
        return 
    
    # ordered values from the tree
    listInOrder = []
    DFSinOrder(t)
    
    return listInOrder[k-1]