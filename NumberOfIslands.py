import collections
import List

'''
Solution to Leetcode question 200
'''
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # edge case: if grid empty then no island
        if(len(grid)==0): return 0

        # initializing variables
        islandCount = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        currentElement = ""

        # loop through all ignoring "0"
        for i in range(rows):
            for j in range(cols):
                currentElement = grid[i][j]                
                if(currentElement == "1" and (i,j) not in visited):
                    
                    self.DFS(i,j,grid,visited)
                    islandCount+=1
                    
        return islandCount
    
    #end numIslands

    def DFS(self, i, j, grid, visited):
        
        # instantiate queue to hold land for the islands, when nothing on queue means no more land to for that island and return and look for another island
        neighboursToVisit = collections.deque()
        firstVertice = (i,j)
        possibleNeighbours = []
        
        # add to current to queue 
        neighboursToVisit.append(firstVertice)
        
        # record that we are looking now at this vertice
        visited.add(firstVertice)
        
        # check the whole island out and stops when there is no more land for this island
        while(len(neighboursToVisit)>0):
            
            # remove from queue
            currentVertice = neighboursToVisit.pop()
            originRow, originCol = currentVertice
                        
            # get vertical and horizontal neighbours 
            possibleNeighbours = [[1,0],[-1,0],[0,-1],[0,1]] # delta position of right,left,down,upper adjacent
            
            # go to that position and if valid push to queue 
            for dr, dc in possibleNeighbours:
                
                currentNeighbour = (originRow + dr, originCol + dc) # this is the position of one of the four adjacent neighbour 
                r, c = currentNeighbour
                #print("visiting neighbour: ", currentNeighbour, " from origin node: ", currentVertice)
                
                # if valid add to queue and visited
                if( r in range(len(grid)) and c in range(len(grid[0]))):                            
                                    
                    if(grid[r][c] == "1"and currentNeighbour not in visited):                    
                        visited.add(currentNeighbour)
                        neighboursToVisit.append(currentNeighbour)
                        #print("part of the island: ", currentNeighbour)
                    
                    #else:
                        #print("Not a 1 or already visited")                        
                #else:
                    #print("===== Not in grid =====")
                    #print("This",currentNeighbour, "is not within", len(grid), "or", len(grid[0]))
            #end for
        #print("Finished traversing an island")
        #end while
    #end DFS
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        