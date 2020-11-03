
# Designing a tree from scratch

class Node():
    def __init__(self,a):
        self.value = a
        self.right = None
        self.left = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
        
    def recursiveInsert(self,current, a):
        
        print('Comparing', a,'to', current.value)
        
        #edge case: duplicate value
        if(a==current.value): 
            print('This is a duplicate value')
            return self
        
        if(a>current.value):
            #check if there's already a node
            print('inserting to the right')
            if(current.right==None):
                print('no right node, inserting now')
                current.right = Node(a)
                return self
            else:
                print('already existing node, repeat')
                current = current.right
                self.recursiveInsert(current,a)
        else:
            print('inserting to the left')
            if(current.left==None):
                print('no left node, inserting now')
                current.left = Node(a)
                return self
            else:
                print('already existing node, repeat')
                current = current.left
                self.recursiveInsert(current,a)
    
    def insert(self,a):
        
        #check if empty tree
        if(self.root==None):
            self.root = Node(a)
            print('empty tree, creating node:', ' ' ,a)
            return self
                    
        #decide to look left/right and check if theres a node 
        current = self.root
        self.recursiveInsert(current,a)
                
            
        

#%% Basic test
tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)
tree.root.left = Node(5)
tree.root.left.left = Node(0)
tree.root.left.right = Node(8)

#%% Testing insert method
tree = BinarySearchTree()

# edge case: empty tree
a = 10
print('inserting: ', a)
out = tree.insert(a)
print('\n')

# test inserting to existing tree
numToInsert = [7, 15, 0, 20, 0]
for i in numToInsert:
    print('inserting: ', i)
    out.insert(i)
    print('\n')
