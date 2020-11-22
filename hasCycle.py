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
        
        print('starting node:', startingNode)
        for neighbour in range(len(adjacencyList[startingNode])):
            
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
                    print(localVisitedNodes)
   
        return hasCycle
    
    # init variables
    visitedNodes = {}
    localVisitedNodes = {}
    startingNode = 0
    
    # initialise starting node as first node
    for i in adjacencyList[0]:
        startingNode = i
        break
    
    return DFS(startingNode, localVisitedNodes)

#%% Testing
    
testMatrix =[[1],\
             [2],\
             [],\
             [1,4],\
             [2,0]]

hasCycle(testMatrix)

testMatrix =[[1,2,3],\
             [2,3],\
             [3],\
             []]

hasCycle(testMatrix)














#%%









