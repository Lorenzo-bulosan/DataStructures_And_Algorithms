
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
                
    def search(self,a):
        # check if empty tree
        if(self.root==None):
            print('empty tree')
            return self   
        
        # check the root node
        if(a == self.root.value):
            print('found at root')
            return a
        
        else:
            current = self.root
            while(True):
                print('comparing',a,'to',current.value)  
                #check right children
                if(a>current.value):
                    print('checking right nodes')
                    
                    if(current.right==None):
                        print('no right node, value not found')
                        return self
                    
                    elif(current.right.value==a):
                        print('found the node')
                        return a
                    
                    else:
                        print('node is',current.right.value,'check next generation')
                        current = current.right
                #check left children
                else:
                    print('checking left nodes')
                    
                    if(current.left==None):
                        print('no left node, value not found')
                        return self
                    
                    elif(current.left.value==a):
                        print('found the node')
                        return a
                    
                    else:
                        print('node is',current.left.value,'check next generation')
                        current = current.left
                    
    def traverseBFS(self):
        
        #queues
        nodesToVisit = []
        listToReturn = []
        
        #edge case empty tree
        if(self.root == None):
            print('Empty list')
            return self
        
        #BFS
        nodesToVisit.append(self.root)
        print('adding:',self.root.value)
        
        while(nodesToVisit):
            
            #dequeue and store in list to return
            current = nodesToVisit.pop(0)
            listToReturn.append(current.value) #returning value instead of list of nodes
            print('removing value:',current.value)
            
            #check child nodes and add to visit list
            if(current.left): 
                print('adding:',current.left.value)
                nodesToVisit.append(current.left)
            
            if(current.right): 
                print('adding:',current.right.value)
                nodesToVisit.append(current.right)
               
        return listToReturn
        
    def traverseDFS_preOrder(self):
        
        # recursive helper function
        def traverse(current):
            listToReturn.append(current.value)
            
            if(current.left):
                traverse(current.left)
                
            if(current.right):
                traverse(current.right)
                
            return
        
        #variables needed
        listToReturn = []
        current = self.root
        
        #edge case empty tree
        if(self.root == None):
            print('Empty list')
            return self
        
        #call recursive function
        traverse(current)
        
        return listToReturn
        

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

#%% test inserting to existing tree
tree = BinarySearchTree()
numToInsert = [10,5,7,20,8,0] #numToInsert = [7, -10, 6.5, 0, 20, 0]
for i in numToInsert:
    print('inserting: ', i)
    tree.insert(i)
    print('\n')

#%% Testing search method, run above section first
valueToFind = 20
out = tree.search(valueToFind)
print('\n')

valueToFind = 999
out = tree.search(valueToFind)
print('\n')

#%% Testing BFS traversal

test = tree.traverseBFS()

## if returning list of nodes
#for i in test:
#    print(i.value)

#returning list of values
print(test)

#%% Testing DFS preOrder

test = tree.traverseDFS_preOrder()
print(test)


