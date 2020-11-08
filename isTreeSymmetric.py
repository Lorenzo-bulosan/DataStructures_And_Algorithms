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

#%% Alternative solution without using list as memory
def isTreeSymmetric2(t):
     
    #check simultaneously both childs
    def check(left,right):
        
        if(left.value!=right.value):
            return False
        
        if(left.left.value!=right.right.value):
            return False
        
        if(left.right.value!=right.left.value):
            return False
        
        check(left.left,left.right)
        check(right.left,right.right)
        
        return True
    
    
    return check(t.left,t.right)

#%% create binary tree for testing
from Trees import *
tree = BinarySearchTree()
numToInsert = [10,5,15,0,8,12,20] 

#populate binary tree
for i in numToInsert:
    print('inserting: ', i)
    tree.insert(i)
    print('\n')
    
#unit test 1--------------------------------
'''correct answer: False'''
