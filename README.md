
# Description
This repository contains algorithms and data structures in python

### Table of contents
* Graphs class
* Hash Table
* Heaps class
* Linked List class
* Queues and Stacks class
* Recursion
* Trees class

#### Graph class
This class contains the following main methods
1. DFS
2. BFS

> Code example:
> adding undirected edges between two vertices in a graph

``` python
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
```