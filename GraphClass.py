
class Graph():

    def __init__(self):
        ''' constructor: empty dictionary of key value pairs
        '''
        self.adjacencyList = {}
        
    def addVertex(self, vertex: str) -> str:
        ''' method that adds a node/vertex
            In: str vertex
            Out: adjacencyList
        '''
        # input type validation
        validInput = isinstance(vertex,str)
        if(not validInput): return 'Invalid input'
        
        # check for duplicate
        try:
            self.adjacencyList[vertex]
            return 'Key already exist'
        except:
            self.adjacencyList[vertex]=[]

        return vertex
            
    
#%% Testing methods
testGraph = Graph()
testGraph.addVertex('testKey')


