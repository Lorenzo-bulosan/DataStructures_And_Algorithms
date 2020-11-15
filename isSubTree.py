#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def parallelCheck(t1,t2):
    
    #stop if no input
    if(t1==None and t2==None):
        return True
        
    #stop if any missing
    if(t1==None or t2==None):
        return False
    
    #continue only if same
    if(t1.value==t2.value):
        return parallelCheck(t1.left,t2.left) and parallelCheck(t1.right,t2.right)

    return False

def isSubtree(t1, t2):
    
    #edge case: empty t2
    if(t2==None):
        return True
        
    #edge case: nothing to compare with
    if(t1==None):
        return False
    
    #return true only in these cases 
    return parallelCheck(t1,t2) or isSubtree(t1.left,t2) or isSubtree(t1.right,t2)