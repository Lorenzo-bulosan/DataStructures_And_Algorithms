
class Graph():

    def __init__(self):
        ''' constructor: empty dictionary of key value pairs
        '''
        self.adjacencyList = {}
        
    def addVertex(self, vertex: str) -> str:
        ''' method that adds a node/vertex
            In: str vertex
            Out: str key added
        '''
        # input type validation
        if(not self.validateInput(vertex,str)): return 'Invalid Input'
        
        # check for duplicate
        try:
            self.adjacencyList[vertex]
            return 'Key already exist'
        except:
            self.adjacencyList[vertex]=[]

        return vertex
    
    def addEdge_undirected(self, vertex1: str, vertex2: str) -> str:
        ''' method that adds an edge/link between two vertices both ways
        '''
        return vertex1 + ' undirected conection to ' + vertex2
        
    def validateInput(self, inputToValidate, typeToValidate) -> bool:
        ''' method that validates input to a given type
            In: all inputToValidate 
                all typeToValidate 
            Out: bool validInput
        '''
        validInput = isinstance(inputToValidate,typeToValidate)
        if(not validInput): return False
        return True
        
        
        
    
#%% Testing methods
testGraph = Graph()
testGraph.addVertex('testKey')


