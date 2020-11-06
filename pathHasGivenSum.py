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
    
    #edge case: empty inputs
    if(current==None or sumToFind==None ):
        return False
     
    #call recursive function
    return traverse(current,sumToFind,totalSum)

#%% Unit Testing
    
#create binary tree for testing
from Trees import *
tree = BinarySearchTree()
numToInsert = [10,5,15,0,8,12,20] 

#populate binary tree
for i in numToInsert:
    print('inserting: ', i)
    tree.insert(i)
    print('\n')

#unit test 1--------------------------------
'''correct answer: True'''
sumToFind = 45
out = hasPathWithGivenSum(tree.root, sumToFind)      
if(out):
    print('test 1 passed')
else:
    print('failed to find path')        
            
#unit test 2--------------------------------
'''correct answer: False'''
sumToFind = 13
out = hasPathWithGivenSum(tree.root, sumToFind)      
if(not out):
    print('test 2 passed')
else:
    print('found a path but no path with given sum exist')   
            

#unit test 3--------------------------------
'''correct answer: False'''
sumToFind = 13
out = hasPathWithGivenSum(None, sumToFind)      
if(not out):
    print('test 3 passed')
else:
    print('failed to identify empty tree')           

#unit test 4--------------------------------
'''correct answer: False'''
sumToFind = None
out = hasPathWithGivenSum(tree.root, sumToFind)      
if(not out):
    print('test 4 passed')
else:
    print('failed to identify incorrect given sum')  
            
            
            
            
            
            
            
            
            
            
            
            
