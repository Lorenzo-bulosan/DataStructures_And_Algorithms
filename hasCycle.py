# Check if graph has a cycle
#
def hasCycle(adjacencyMatrix: list) -> bool:
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
        
        for neighbour in range(len(adjacencyMatrix[startingNode])):
            if(adjacencyMatrix[startingNode][neighbour]==1):

                # base case
                if(neighbour in localVisitedNodes): 
                    print('found cycle')
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
    startingNode = 0
    
    # initialise starting node as first node
    for i in adjacencyMatrix[0]:
        startingNode = i
        break
    
    return DFS(startingNode, localVisitedNodes)

#%% Testing
    
testMatrix =[[0,1,0,1,0],\
             [0,0,1,0,0],\
             [0,0,0,0,0],
             [0,1,0,0,1],
             [1,0,1,0,0]]

hasCycle(testMatrix)














#%%









