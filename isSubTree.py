#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    
    def parallelCheck(t1,t2):
        
        #stop as soon as not the same
        if(t1.value!=t2.value):
            return False
        else:
            # reaches leaf node
            if(t1.left==None and t1.right==None and t2.left==None and t2.right==None):
                if(t1.value==t2.value):
                    return True
            
            if(t1.left!=None and t2.left!=None):
                parallelCheck(t1.left,t2.left)
                
            if(t1.right!=None and t2.right!=None):
                parallelCheck(t1.right,t2.right)           
                
        return
    
    #edge case: empty t2
    if(t2==None):
        return True
        
    #edge case: nothing to compare with
    if(t1==None):
        return False
    
    #return true only in these cases
    if(t1==t2):
        return True
        
    checkLeft = parallelCheck(t1.left,t2)
    if(checkLeft==True):
        return True
        
    checkRight = parallelCheck(t1.right,t2)
    if(checkRight==True):
        return True
    
    return False
    
    
return
