# find number of critical edges
#
#
#
#%% 
def singlePointOfFailure(connections: list) -> int:
    ''' method for finding the critical edges
        In: int[][] adjacency matrix of graph
        Out: int Number of critical edges
    '''
    numberOfIslands = 0
    criticalEdges = 0
    matrixTmp = connections[:]
    visitedNodes = {}
    
    # for every node
    for node in range(len(connections)):
        
        if(not node in visitedNodes): visitedNodes[node] = True
        
        for neighbour in range(len(connections[node])):
            if(connections[node][neighbour]==1):
                if(not neighbour in visitedNodes):
                    
                    visitedNodes[neighbour] = True
                    
                    print('removing edge between:',node,neighbour)
                    # remove edge from matrix and check
                    matrixTmp[node][neighbour] = 0
                    matrixTmp[neighbour][node] = 0
                    
                    # if still one component after removing edge then not critical edge
                    numberOfIslands = findNumberOfIslands(matrixTmp)
                    print('removing:',neighbour,'breaks into',numberOfIslands)
                    
                    if(numberOfIslands>1): 
                        print('count this edge')
                        criticalEdges+=1      
                        
                    # reverse the change for next iteration
                    matrixTmp[node][neighbour] = 1
                    matrixTmp[neighbour][node] = 1
                
    print(criticalEdges)
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
        edge = ''
        for neighbour in range(len(connections[startingNode])):
            if(connections[startingNode][neighbour]==1):
                
                #edge = str(node)+str(neighbour)
                if(not neighbour in visitedList):
                    visitedList[neighbour] = True
                    dfs(neighbour)
        return 
    
    visitedList = {}
    numberOfIslands = 0
    
    # check all nodes but 
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

#findNumberOfIslands(testMatrix)
#print(testMatrix)
#singlePointOfFailure(testMatrix)
#numberOfIslands = findNumberOfIslands(testMatrix)
#print('number of connected components:',numberOfIslands)


















#%%