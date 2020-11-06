def hasPathWithGivenSum(t, s):

    def traverseAndSum(current,s):
        
        s = s-current.value
        print('current sum:',s)
        
        # check if leaf node
        if(current.left==None and current.right==None):
            print('leaf node')
            # check sum
            if(s==0): 
                return True
        
        # not leaf
        elif(current.left or current.right):
            #check left path
            if(current.left):
                print('checking left')
                traverseAndSum(current.left,s)
            
            #check right path
            if(current.right):
                print('checking right')
                traverseAndSum(current.right,s)
                
        else:
            return False
        
    # check for empty tree
    if(t):
        # call recursive helper function and return output
        return traverseAndSum(t,s)
    else:
        return False

