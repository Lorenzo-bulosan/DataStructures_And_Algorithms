
class Tree(object):
   def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None
     
def restoreBinaryTree(inorder, preorder):
    ''' restores binary tree from 2 traversed list
    
    In: int[] inOrder,
        int[] preOrder
    Out: TreeNode root node
    '''
    def helperRestore(startIdxPreOrder,startIdxInOrder,endIdxInOrder,inOrderList,preOrderList):
        ''' recursive helperfunction that divides the list and sets head node
        
        In: int start idx of preOrderList, 
            int start idx of inOrderList,
            int end idx of inOrderList,
            int[] preOrderList
            int[] inOrderList
        Out: TreeNode root node
        '''
        # check for boundaries on the indexs
        if(startIdxPreOrder >= len(inOrderList)):
            print('exit 1')
            return None
        
        if(startIdxInOrder > endIdxInOrder):
            print('exit 2')
            return None
        
        # check empty lookup list
        if(not inOrderList[startIdxInOrder:endIdxInOrder]):
            print('exit 3',[startIdxInOrder,endIdxInOrder])
            return None
     
        # set head as the next in the list postOrder
        head = preOrderList[startIdxPreOrder]
        tree = Tree(head)
        print('head is:',head)
        
        # find head index inside inOrderList within given range
        print('looking between:',[startIdxInOrder,endIdxInOrder],'resulting in:',inOrderList[startIdxInOrder:endIdxInOrder])
        headIdx = 0
        for i in range(startIdxInOrder,endIdxInOrder):
            if(inOrderList[i]==tree.value):
                headIdx = i
                break
        print('found head at idx:',headIdx)
            
        # set left node: next head is next in preOrder, end of inOrder=current head idx
        tree.left = helperRestore(startIdxPreOrder+1,startIdxInOrder,headIdx,\
                                  inOrderList,preOrderList)
        

        # set left node, next head is the same (startIdxPreOrder+1) 
        #   but also skipping all the left nodes = (headIdx-startIdxInOrder)
        # the range of the list to look = head:end
        print('right head starting at index',startIdxPreOrder+1+headIdx-startIdxInOrder)
        tree.right = helperRestore(startIdxPreOrder+1+headIdx-startIdxInOrder,headIdx+1,endIdxInOrder,\
                                 inOrderList,preOrderList)
        
        return tree
    
    # initial values
    startIdxPreOrder = 0
    startIdxInOrder = 0
    endIdxInOrder = len(inorder)
    inOrderList = inorder
    preOrderList = preorder
    
    # visualize both list
    print('inOrder:',inOrderList)
    print('preOrder:',preOrderList)
    
    # call recursive helper function
    tree = helperRestore(startIdxPreOrder,startIdxInOrder,endIdxInOrder,inOrderList,preOrderList)
    
    return tree

#%% 
inOrderList = [0,5,7,10,15,20]
preOrderList = [10,5,0,7,15,20]
tree = restoreBinaryTree(inOrderList, preOrderList)