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
        for neighbour in adjacencyList[startingNode]:
                print('checking neighbour:',neighbour,'from node',startingNode)
                print(localVisitedNodes)
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
                    print('deleting neighbour:',neighbour)
                    print(localVisitedNodes)
            
        print('returning------------',hasCycle)
        return hasCycle
    
    # init variables
    visitedNodes = {}
    localVisitedNodes = {}

    # loop the adjacency list
    for node in range(len(adjacencyList)):
        print('NODE======',node)
        hasCycle = DFS(node, localVisitedNodes)
        localVisitedNodes.pop(node)
        if hasCycle: return True

    return hasCycle

#%% Testing
    
testMatrix =[[1,4,3],\
             [],\
             [1,4,3],\
             [1],\
             [3]]

hasCycle(testMatrix)

#testMatrix =[[1,2,3],\
#             [2,3],\
#             [3],\
#             []]
#
#print(hasCycle(testMatrix))














#%%









