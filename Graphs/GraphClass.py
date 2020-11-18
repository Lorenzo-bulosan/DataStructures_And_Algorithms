
class Graph():

    def __init__(self):
        ''' constructor: empty dictionary of key value pairs
        '''
        self.adjacencyList = {}
        
    def __validateInput(self, inputToValidate, typeToValidate) -> bool:
        ''' method that validates input to a given type or isEmpty
            In: all inputToValidate 
                all typeToValidate 
            Out: bool validInput
        '''
        # empty input handling
        if(not inputToValidate or not typeToValidate):
            return False
        
        # type validation
        validInput = isinstance(inputToValidate,typeToValidate)
        if(not validInput): return False
        
        return True
        
    def __checkVertex(self, vertex: str) -> bool:
        ''' method that validates if vertex exist in graph
            In: str vertex 
            Out: bool validInput
        '''
        # input type validation
        if(not self.__validateInput(vertex,str)): return False
        
        # try calling for key, throws error if key does not exist
        try:
            self.adjacencyList[vertex]
            return True
        
        except:
            return False
    
    def hasEdgeBetween(self, vertex1: str, vertex2: str) -> bool:
        ''' method that checks weather vertex 1 has an edge to vertex 2
            In: str vertex1
                str vertex2
            Out: bool
        '''
        # input type validation
        if(not self.__validateInput(vertex1,str)): return False
        if(not self.__validateInput(vertex2,str)): return False
        
        # check if vertex/nodes exist
        if(not self.__checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.__checkVertex(vertex2)): return 'vertex2 not in graph'
        
        # check inside vertex 1 for vertex 2
        for i in self.adjacencyList[vertex1]:
            if(i==vertex2):
                return True
        
        return False
        
    def addVertex(self, vertex: str) -> str:
        ''' method that adds a node/vertex
            In: str vertex
            Out: str key added
        '''
        # input type validation
        if(not self.__validateInput(vertex,str)): return 'Invalid Input'
        
        # check for duplicate
        if(self.__checkVertex(vertex)): return 'Key already exist'
        
        # add to adjacencyList
        self.adjacencyList[vertex]=[]

        return vertex
    
    def addEdge_undirected(self, vertex1: str, vertex2: str) -> str:
        ''' method that adds an edge/link between two vertices both ways
            In: str vertex1
                str vertex2
            Out: str result
        '''
        # validate both inputs
        if(not self.__validateInput(vertex1,str)): return 'Invalid Input'
        if(not self.__validateInput(vertex2,str)): return 'Invalid Input'
        
        # check if vertex/nodes exist
        if(not self.__checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.__checkVertex(vertex2)): return 'vertex2 not in graph'
        
        # check if already connected between each other
        if(self.hasEdgeBetween(vertex1,vertex2) and self.hasEdgeBetween(vertex1,vertex2)): 
            return 'vertexes already connected'
        
        # add two way connection
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)
        
        return '"'+vertex1+'"' + ' undirected conection to ' + '"'+vertex2+'"'
        
    def removeEdgeBetween(self,vertex1: str, vertex2: str) -> str:
        ''' method that removes link between given vertices
            In: str vertex1
                str vertex2
            Out: str result
        '''
        # validate both inputs
        if(not self.__validateInput(vertex1,str)): return 'Invalid Input'
        if(not self.__validateInput(vertex2,str)): return 'Invalid Input'
        
        # check if vertex/nodes exist
        if(not self.__checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.__checkVertex(vertex2)): return 'vertex2 not in graph'

        # check if not connected 
        if(not self.hasEdgeBetween(vertex1,vertex2) and not self.hasEdgeBetween(vertex2,vertex1)):
            return 'no edge between these two vertexes'
        
        # access all edges of vertex1 and remove vertex2
        for i in self.adjacencyList[vertex1]:
            if(i==vertex2):
                self.adjacencyList[vertex1].remove(vertex2)
                break
            
        # access all edges of vertex2 and remove vertex1
        for j in self.adjacencyList[vertex2]:
            if(j==vertex1):
                self.adjacencyList[vertex2].remove(vertex1)
                break
            
        return '"'+vertex1+'"' + ' no longer connected to ' + '"'+vertex2+'"'
        
    def removeVertex(self,vertex: str) -> str:
        ''' method that removes a vertex and all conections to it from a graph
            In: str vertex to be removed
            Out: str result
        '''
        # input validation
        if(not self.__validateInput(vertex,str)): return 'Invalid Input'
        
        # check vertex exist
        if(not self.__checkVertex(vertex)): return 'vertex not in graph'
              
        # remove links in other nodes that point to this vertex
        for key in self.adjacencyList:
            self.removeEdgeBetween(key,vertex)
       
        # remove vertex itself from graph
        self.adjacencyList.pop(vertex)     
        
        return 'removed'+vertex+'from graph'
    
    def traverseDFS(self) -> list :
        ''' method to traverse the graph using DFS algorythm
            In: None
            Out: str[] visited nodes
        '''
        def helperDFS(startingVertex: str) -> None:
            ''' recursive helper method to traverse DFS
                In: str vertex
                Out: list resultsList
            '''
            # base condition
            if(startingVertex==None):
                return None
                        
            # add vertex to results list
            resultsList.append(startingVertex)
            
            # mark as visited
            visitedNodes[startingVertex] = True
            
            # traverse into current neighbours if not visited
            for neighbour in self.adjacencyList[startingVertex]:
                if(not neighbour in visitedNodes):
                    helperDFS(neighbour)
                
            # if nothing to visit return None
            return None
                
        # check if list is empty
        if(not len(self.adjacencyList)>0): return False
        
        # set starting vertex as the first key in adjacency list
        for i in self.adjacencyList:
            startingVertex = i
            break
        
        visitedNodes = {}
        resultsList =[]
        
        # call helper function
        helperDFS(startingVertex)
        
        return resultsList
#%% Testing methods

test = Graph()

# add nodes
test.addVertex('a')
test.addVertex('b')
test.addVertex('c')
test.addVertex('d')
test.addVertex('e')

# add edge between 'a' and 'b' 
test.addEdge_undirected('a','b')
test.addEdge_undirected('a','c')
test.addEdge_undirected('b','c')
test.addEdge_undirected('c','d')
test.addEdge_undirected('e','a')

# test to handle already existing link
test.addEdge_undirected('a','b')
    
# test remove edges
#test.removeEdgeBetween('a','c') 

# test removing a node from the graph
#print(test.adjacencyList)
#test.removeVertex('c')
#print(test.adjacencyList)

# test DFS traversal
allNodes = test.traverseDFS()
print(allNodes)


