#%% passes only 7/8 test
def hasPathWithGivenSum(t, s):
    '''input:node, sum to find
    returns bool
    '''

    # recursive helper function
    def traverse(current,sumToFind,totalSum):
        '''input: node, sum to find, total sum
        returns bool
        '''
        # add to current sum
        totalSum = totalSum+current.value
        
        #check if leaf node and return if target sum
        if(current.left==None and current.right==None):
            if(totalSum==sumToFind): return True
                
        #not leaf node check left pathway
        if(current.left):
            out = traverse(current.left,sumToFind,totalSum)
            if(out): return True #stop the recursion if path found
        
        #not leaf node check right pathway
        if(current.right):
            out = traverse(current.right,sumToFind,totalSum)
            if(out): return True #stop the recursion if path found
        
        return False
    
    #renaming for readability
    current = t
    sumToFind = s
    totalSum = 0
    
    #edge case empty tree
    if(t == None):
        print('Empty list')
        return False
    
    #call recursive function
    return traverse(current,sumToFind,totalSum)

#%% Creating tree to test
from Trees import *
tree = BinarySearchTree()
numToInsert = [10,5,15,0,8,12,20] 
#numToInsert = [7, -10, 6.5, 0, 20, 0]

for i in numToInsert:
    print('inserting: ', i)
    tree.insert(i)
    print('\n')

# Testing function
sumToFind = 38
out = hasPathWithGivenSum(tree.root, sumToFind)            
print(out)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
