# Do all cities have cycles?
# input graph represented as matrix of where elements have values 'false' or 'true'
# has n=rows and m=columns representing all possible connections
# if matrix[n][m]=True then city 'n' points to city 'm'
#
# QUESTION: determine if all cities 'n' have cycles
# matrixInput = [['false','true','false','false'],
#                ['false','false','true','false'],
#                ['true','false','false','true'],
#                ['false','false','true','false']]
# answer: True
#
def areCitiesConnected(roadRegister: list) -> bool:
    ''' method to find if all cities have cycles
        In: bool[][] adjacency matrix of cities
        Out: bool returns True if all cities can be cycled
    '''
    def helperDFS(city: int) -> None: 
        ''' helper method that performs DFS given a city and keeps track of visited ones
            In: int city node
            Out: None
        ''' 
        for neighbour in range(len(roadRegister[city])):  
            
            # go to road
            isNeighbour = roadRegister[city][neighbour]
            
            if(isNeighbour=='true'): 
                
                print('found road to dfs:', neighbour)
                
                if(not neighbour in visitedCity):
                    
                    visitedCity[neighbour]=True
                    helperDFS(neighbour)  
                    print('DFS into:', city)
                    
                else:
                    print("can't dfs, already seen:",neighbour)
                    print('trying next road')
                    hasCycle[neighbour]=True
                    return
            else:
                print('no road here:', [neighbour,isNeighbour])
        return
    # --- END OF HELPER FUNCTION: helperDFS
    
    # look up tables to keep track of visited cities and cycles
    visitedCity = {}
    hasCycle = {}
    
    # check for cycle at each row = city
    for city in range(len(roadRegister)):
        
        # keep record that visited
        print('checking roads at city:',city)
        visitedCity[city] = True
        
        # DFS into each neighbour
        for neighbour in range(len(roadRegister[city])):
            
            # simplify
            isNeighbour = roadRegister[city][neighbour]
            
            # find road and visit the next city
            if(isNeighbour == 'true'):
            
                if(not neighbour in visitedCity):
                    helperDFS(neighbour)

                print('already been to:', neighbour)
                print(neighbour,'CITY HAS CYCLE---------')
                hasCycle[neighbour]=True
        
    # check if all cities have cycles i.e hasCycles has to have all cities therefore check matrix length
    if(len(hasCycle)==len(roadRegister)):
        print('all cities have cycles')
        print(hasCycle)
        return True
        
    else:
        print('not all cities have cycles')
        print(hasCycle)
        return False
    
#%% Test 1
roadRegister1 = [['false','true','false','false'],\
                ['false','false','true','false'],\
                ['true','false','false','true'],\
                ['false','false','true','false']]

result1 = areCitiesConnected(roadRegister1)

if result1==True: print('passed')
else: print('failed')

#%% Test 2
roadRegister2 = [['false','false','false','false'],\
                ['false','false','true','false'],\
                ['true','false','false','true'],\
                ['false','false','true','false']]

result2 = areCitiesConnected(roadRegister2)

if result2==False: print('passed')
else: print('failed')

#%% Test 3
roadRegister3 = [['false','true','true','true','true'],\
                ['true','false','true','true','true'],\
                ['true','true','false','true','true'],\
                ['true','true','true','false','true'],\
                ['true','true','true','true','false']]

result3 = areCitiesConnected(roadRegister3)
if(result3 == True): print('passed')
else: print('failed')