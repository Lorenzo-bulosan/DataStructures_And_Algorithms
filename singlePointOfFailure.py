# Find number of critical edges:
# Given the adjacency matrix of a graph find the number of critical edges
# Defenition of Critical Edges: edges that if removed results in the graph 
# being in two or more components or islands
#
def singlePointOfFailure(connections: list) -> int:
    ''' method for finding the critical edges
        In: int[][] adjacency matrix of graph
        Out: int Number of critical edges
    '''
    numberOfIslands = 0
    criticalEdges = 0
    matrixTmp = connections[:]
    visitedNodes = {}
    
    # for every node remove edge and count number of islands
    for node in range(len(connections)):
        
        if(not node in visitedNodes): 
            visitedNodes[node] = True
            
        for neighbour in range(len(connections[node])):
            
            if(connections[node][neighbour]==1):
                
                if(not neighbour in visitedNodes):
                    
                    # remove edge from matrix and check
                    matrixTmp[node][neighbour] = 0
                    matrixTmp[neighbour][node] = 0
                    
                    # if still one component after removing edge then not critical edge
                    numberOfIslands = findNumberOfIslands(matrixTmp)
                    
                    if(numberOfIslands>1): criticalEdges+=1      
                        
                    # reverse the change for next iteration
                    matrixTmp[node][neighbour] = 1
                    matrixTmp[neighbour][node] = 1
                
    return criticalEdges

def findNumberOfIslands(connections: list) -> int:
    ''' method to count number of components in a graph
        In: int[][] adjacencyMatrix of graph
        Out: int number of components
    '''
    def dfs(startingNode: int) -> None:
        ''' helper method to traverse to all neighbours of a node
            In: int starting Node
            Out: None
        '''
        for neighbour in range(len(connections[startingNode])):
            
            if(connections[startingNode][neighbour]==1):

                if(not neighbour in visitedList):
                    visitedList[neighbour] = True
                    dfs(neighbour)
        return 
    
    visitedList = {}
    numberOfIslands = 0
    
    # if it can be traversed completely then iterations will be only 1 because of visited list
    for node in range(len(connections)):
        if(not node in visitedList):
            numberOfIslands += 1
            dfs(node)
            
    return numberOfIslands


#%% Test finding number of components = islands

testMatrix= [[0,1,1,0,0,0,0], 
             [1,0,1,0,0,0,0], 
             [1,1,0,0,0,0,1], 
             [0,0,0,0,1,1,1], 
             [0,0,0,1,0,1,0], 
             [0,0,0,1,1,0,0], 
             [0,0,1,1,0,0,0]]

correctAnswer = 2
numberOfCriticalEdges = singlePointOfFailure(testMatrix)

if(numberOfCriticalEdges == correctAnswer):
    print('Test 2 Passed')
else:
    print('Test 1 Failed')
















#%%