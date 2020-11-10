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
print('\n')
correct = 15
pos = 6
t = tree1.root

if(kthSmallestInBST(t,pos)==correct):
    print('Test 1 Passed')
else:
    print('The wrong answer:',kthSmallestInBST(t,pos))
    print('Failed to identify correct answer')

print('Test 1 finished\n')