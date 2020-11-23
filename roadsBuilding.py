# Given a undirected graph
# find the missing edges and return as list of pairs 
# ordered lexicographically
# e.g InList = [[0,1],[1,2],[2,0]] totalNodes = 4
# then the missing pairs are [[0, 3], [1, 3], [2, 3]]

def roadsBuilding(cities: int, roads: list) -> list:
    ''' check that all cities are connected (undirected)
        In: int cities or nodes
        Out: int[][] of currently connected nodes ordered lexicographically
    '''
    # initialize adjacency matrix
    adjacencyMatrix = []
    columns = []
    for i in range(cities): columns.append(False)
    for i in range(cities): 
        newColum = columns[:] #important deep copy because if not the list will have same reference
        adjacencyMatrix.append(newColum)

    # build the adjacency matrix
    node = 0
    neighbour = 0
    for pair in roads:
        
        node = pair[0]
        neighbour = pair[1]
        adjacencyMatrix[node][neighbour] = True
        adjacencyMatrix[neighbour][node] = True
    
    # build results list
    resultsList = []
    missingPair = []
    elementValue = ''
    for row in range(len(adjacencyMatrix)):
        for neighbour in range(len(adjacencyMatrix)):
            
            elementValue = adjacencyMatrix[row][neighbour]
            if(neighbour!=row and elementValue==False):
                
                # build results list
                missingPair = [row,neighbour]
                resultsList.append(missingPair)
                
                # update matrix
                adjacencyMatrix[row][neighbour] = True
                adjacencyMatrix[neighbour][row] = True

    return resultsList

#%%