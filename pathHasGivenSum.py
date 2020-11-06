
#%% passes only 7/8 test
def hasPathWithGivenSum2(t, s):

    def traverseAndSum(current,s,currentSum):
        
        print('current sum:',currentSum,'node value:',current.value)
        currentSum = currentSum+current.value
        print('total',currentSum)
        
        # check if leaf node
        if(current.left==None and current.right==None):
            print('leaf node')
            # check sum
            if(s==currentSum): 
                print('found path')
                return True

        #check left path
        elif(current.left):
            print('checking left')
            return traverseAndSum(current.left,s,currentSum)
                 
        #check right path
        elif(current.right):
            print('checking right')
            return  traverseAndSum(current.right,s,currentSum)
              
        return False
        
    # check for empty tree
    if(t):
        # call recursive helper function and return output
        currentSum = 0
        return traverseAndSum(t,s,currentSum)
    else:
        return False

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
sumToFind = 15
out = hasPathWithGivenSum(tree.root, sumToFind)            
print(out)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
