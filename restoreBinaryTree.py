
class Tree(object):
   def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None
     
def restoreBinaryTree(inorder, preorder):
    
    # instantiate tree
    tree = Tree(0)
    inOrder = inorder
    preOrder = preorder
 
    # find idx head in inOrder
    head = 10
    inOrder_head_idx = 0
    
    for i in inOrder:
        if(i==head):
            break
        inOrder_head_idx += 1
        
    tree.value = head
    print('preOrder head idx:',inOrder_head_idx)
    
    # divide nodes left/right from head as center
    inStart = 0
    inEnd = len(inOrder)
    leftNodes = inOrder[inStart:inOrder_head_idx]
    rightNodes = inOrder[len(leftNodes)+1:inEnd]
    
    print(preOrder)
    print(leftNodes)
    print(rightNodes)
    
    #find head from leftNodes by looking up preOrder
    for i in leftNodes:
        for j in preOrder:
            if(i==j):
                leftNewHead = j
            
    print('head in left:',leftNewHead)
    
    tree.left = leftNewHead
    
    #find head from rightNodes by looking up preOrder
    for i in rightNodes:
        for j in preOrder:
            if(i==j):
                rightNewHead = j
            
    print('head in right:',rightNewHead)
    
    return tree

#%% Test
    
inOrder = [0,5,10,7,15,20]
preOrder = [10,5,0,7,15,20]

restoreBinaryTree(inOrder, preOrder)
