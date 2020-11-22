# Check if graph has a cycle
#
def hasCycle(adjacencyList: list) -> bool:
    ''' method to find a cycle in the graph
        In: int[][] graph's adjacency matrix
        Out: bool True if graph has a cycle
    '''    
    def DFS(startingNode: int ,localVisitedNodes: dict) -> bool:
        ''' recursive helper function to traverse the graph using DFS
            In: int node to start
                bool{} look up table for visited nodes
            Out: None
        '''
        hasCycle = False
        localVisitedNodes[startingNode]=True  
        
        for neighbour in adjacencyList[startingNode]:

                # base case
                if(neighbour in localVisitedNodes): 
                    hasCycle = True
                    break 
                
                # not visited
                else:
                    # add to visited
                    visitedNodes[neighbour] = True
                    out = DFS(neighbour,localVisitedNodes)    
                    if(out): return True

                    # backtrack
                    localVisitedNodes.pop(neighbour)  
                    
        return hasCycle
    
    # init variables
    visitedNodes = {}
    localVisitedNodes = {}
    
    # check for cycle at every node start
    for node in range(len(adjacencyList)):
        
        hasCycle = DFS(node, localVisitedNodes)
        localVisitedNodes.pop(node)
        
        if hasCycle: return True # early stopping

    return hasCycle

#%% Testing 1 ---------------------------------
'''Correct answer: False'''
testMatrix =[[1,4,3],\
             [],\
             [1,4,3],\
             [1],\
             [3]]

print('has cycle:',hasCycle(testMatrix))

#%% Testing 2 ---------------------------------
'''Correct answer: False'''
testMatrix =[[1,2,3],\
             [2,3],\
             [3],\
             []]

print('has cycle:',hasCycle(testMatrix))

#%% Testing 3 ---------------------------------
'''Correct answer: True'''
testMatrix =[[], 
             [0,2], 
             [4,0], 
             [0], 
             [0,3], 
             [3], 
             [7], 
             [5], 
             [7,6], 
             [8,11], 
             [9], 
             [10]]

print('has cycle:',hasCycle(testMatrix))
















#%%









