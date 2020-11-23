# Check all nodes are within 2 steps each
# given a undirected graph

def areAllNodesWithinKreach(numNodes: int, roads: list) -> bool:
    ''' method to check that all nodes are within 2 steps of each other
        In: int number of total nodes
        Out: int[][] information on what nodes are connected
    '''
    def helperDFS(startingNode: int, visitedList: dict, parentNode:int, stepsTaken: int) -> list:
        ''' recursive helper function to traverse graph 2 steps
            In: int starting node
                int{} visited list look up table 
                int parentNode
            Out: int[] containing neighbours that are within 2 steps
        '''
        print('DFS on:',startingNode)

        # base condition
        if(stepsTaken==2): 
            print('starting node reaches:', nodesReach)
            print('2 steps, currently in:', startingNode,'--------------')
            return True
        
        # adds starting node as key in 
        if(not startingNode in visitedList): visitedList[startingNode] = True

        print('visitedList:',visitedList)
        print('starting node reaches:', nodesReach)
        
        for i in range(len(adjacencyList[startingNode])):
            neighbour = adjacencyList[startingNode][i]
            print('checking neighbour:',neighbour,'from node:',startingNode)
            
            if(not neighbour in visitedList): 
                stepsTaken += 1
                print('taking step:',stepsTaken,'and reach',neighbour)
                
                visitedList[neighbour] = True
                nodesReach[parentNode].append(neighbour)
                out = helperDFS(neighbour,visitedList,parentNode,stepsTaken)
                
                if(out): 
                    visitedList.pop(neighbour)  
                    print('deleting neighbour',neighbour)
                    print(visitedList)
                
                stepsTaken -= 1
       
            print('already seen neighbour:', neighbour)

        print('reach end of neighbours of node:', startingNode)
        
        return
        
    # init look up tables
    nodesReach = {}
    adjacencyList = {}
    visitedList = {}
    stepsTaken = 0
    
    # build adjacency list
    node = 0
    neighbour = 0
    for pair in roads:
        
        node = pair[0]
        neighbour = pair[1]
        
        # build undirected graph
        if(not node in adjacencyList): adjacencyList[node] = []
        if(not neighbour in adjacencyList): adjacencyList[neighbour] = []
        
        adjacencyList[node].append(neighbour)
        adjacencyList[neighbour].append(node)
        
    # DFS into every node of the list
    node = 0
    for node in range(len(adjacencyList)):
        print('Outside, goint to DFS on:',node,'===========')
        nodesReach[node] = []
        helperDFS(node, visitedList, node, stepsTaken)
        visitedList = {}
        stepsTaken = 0
    
    print('final node reach',nodesReach)
    
    for node in range(len(nodesReach)): 
        if(len(nodesReach[node])!=numNodes-1): return False
        
    return True


#%% Test
numNodes = 4
roads = [[0,4],\
         [5,0],\
         [2,1],\
         [1,4],\
         [2,3],\
         [5,2],\
         ]
result = areAllNodesWithinKreach(numNodes, roads)
print(result)

















#%%