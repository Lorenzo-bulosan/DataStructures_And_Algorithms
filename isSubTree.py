#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    
    def DFSpreOrderParallelCheck(tree1,tree2):
        
        print([tree1.value,tree2.value])
        
        # exit as soon as not the same
        if(tree1.value!=tree2.value): 
            return False
        
        # if same value check the rest of the tree
        else:
            if(tree1.left!=None and tree2.left!=None):
                DFSpreOrderParallelCheck(tree1.left,tree2.left)
                        
            if(tree1.right!=None and tree2.right!=None):
                DFSpreOrderParallelCheck(tree1.right,tree2.right)        
            
            return True

    def DFSpreOrder(tree1,tree2):
        
        print('cheking first tree:',tree1.value,tree2.value)
        
        result = False
        
        if(tree1.value==tree2.value):
            result = DFSpreOrderParallelCheck(tree1,tree2)
            return result
    
        #check left
        print('checking left')
        if(tree1.left!=None and result==False):
            DFSpreOrder(tree1.left,tree2)
        
        #check right
        print('checking right')
        if(tree1.right!=None and result==False):
            DFSpreOrder(tree1.right,tree2)
         
        return result  
        
    #edge case: t1 empty
    if(t1==None and t2!=None):
        return False
    
    #edge case: t2 empty
    if(t2==None and t1!=None):
        return True
    
    #edge case: both inputs emtpy
    if(t1==None and t2==None):
        return True
    
    
    return DFSpreOrder(t1,t2)
