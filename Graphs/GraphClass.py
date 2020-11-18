
class Graph():

    def __init__(self):
        ''' constructor: empty dictionary of key value pairs
        '''
        self.adjacencyList = {}
        
    def validateInput(self, inputToValidate, typeToValidate) -> bool:
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
        
    def checkVertex(self, vertex: str) -> bool:
        ''' method that validates if vertex exist in graph
            In: str vertex 
            Out: bool validInput
        '''
        # try calling for key, throws error if key does not exist
        try:
            self.adjacencyList[vertex]
            return True
        
        except:
            return False
        
    def addVertex(self, vertex: str) -> str:
        ''' method that adds a node/vertex
            In: str vertex
            Out: str key added
        '''
        # input type validation
        if(not self.validateInput(vertex,str)): return 'Invalid Input'
        
        # check for duplicate
        if(self.checkVertex(vertex)): return 'Key already exist'
        
        # add to adjacencyList
        self.adjacencyList[vertex]=[]

        return vertex
    
    def addEdge_undirected(self, vertex1: str, vertex2: str) -> str:
        ''' method that adds an edge/link between two vertices both ways
        '''
        # validate both inputs
        if(not self.validateInput(vertex1,str)): return 'Invalid Input'
        if(not self.validateInput(vertex2,str)): return 'Invalid Input'
        
        # check if vertex/nodes exist
        if(not self.checkVertex(vertex1)): return 'vertex1 not in graph'
        if(not self.checkVertex(vertex2)): return 'vertex2 not in graph'
        
        # add two way connection
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)
        
        return '"'+vertex1+'"' + ' undirected conection to ' + '"'+vertex2+'"'
        
            
        
#%% Testing methods

test = Graph()

    
    
    

    


