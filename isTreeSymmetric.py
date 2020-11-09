def isTreeSymmetric2(t):
     
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

#%% Alternative solution without using list as memory
def isTreeSymmetric(t):
     
    def checkSubTree(subLeft,subRight):
           
        # check if leaf node
        if(subLeft==None and subRight==None):
            return True
        
        #check that both exist
        elif(subLeft!=None and subRight!=None):
            
            #value check and recursion
            return subLeft.value==subRight.value and \
                   checkSubTree(subLeft.left,subRight.right) and \
                   checkSubTree(subLeft.right, subRight.left)
       
        return False        
    
        # alternative way of re-writting
        
        #    if(subLeft.value==subright.value):
        #        if(checkSubTree(subLeft.left,subright.right)):
        #            if(checkSubTree(subLeft.right,subright.left)):
        #                return True
        
    # check root isEmpty
    if(t == None):
        return True
    
    return checkSubTree(t.left,t.right)

#%% create binary tree for testing
print('Conducting Test 1')
print('creating test tree')
from Trees import *
tree1 = BinarySearchTree()
numToInsert = [10,5,15,0,8,12,20] 

#populate binary tree
for i in numToInsert:
    tree1.insert(i)
    
#unit test 1--------------------------------
'''correct answer: False'''
if(isTreeSymmetric(tree1.root)==False):
    print('Test 1 Passed')
else:
    print('Failed to identify incorrect symmetry')

print('Test 1 finished\n')
    
#%% create binary tree for testing
print('Conducting Test 2')
print('creating test tree')
from Trees import *
tree2 = BinarySearchTree()
numToInsert = [10] 

#populate binary tree
for i in numToInsert:
    tree2.insert(i)

#unit test 2--------------------------------
'''correct answer: True'''
if(isTreeSymmetric(tree2.root)==True):
    print('Test 2 Passed')
else:
    print('Failed to identify tree with only one node')

print('Test 2 finished\n')

#%% create binary tree for testing
print('Conducting Test 3')
print('creating test tree')

tree3 = None
 
#unit test 3--------------------------------
'''correct answer: True'''
if(isTreeSymmetric(tree3)==True):
    print('Test 3 Passed')
else:
    print('Failed to identify tree with only one node')

print('Test 3 finished\n')