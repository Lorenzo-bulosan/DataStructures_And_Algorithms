'''
Solution to leetcode Q417
'''
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rLength, cLength = len(heights), len(heights[0])
        vstPacific, vstAtl = set(), set()
        
        #print(self.rLength, self.cLength)

        #================================================================================
        def dfs(r, c, prevHeight, vst):

            # out of bounds
            if(r < 0 or c < 0 or r >= rLength or c >= cLength) : #print('out of bounds')
                return

            # already visited
            if( (r,c) in vst ): # print('already visited')
                return

            # lower than previous
            if( prevHeight > heights[r][c] ): # print(prevHeight, heights[r][c])
                return

            # add to visit
            vst.add((r,c))

            # dfs into neighbors
            dfs(r+1, c, heights[r][c], vst)
            dfs(r-1, c, heights[r][c], vst)
            dfs(r, c+1, heights[r][c], vst)
            dfs(r, c-1, heights[r][c], vst)
            
        # end dfs
        #================================================================================

        # dfs in vertical oceans starting top and bottom cols to dfs
        r = 0
        rLast = rLength - 1
        
        for c in range(cLength):
            
            currentTopRowHeight = heights[r][c]
            dfs(r, c, currentTopRowHeight, vstPacific)
            
            currentLastRowHeight = heights[rLast][c]
            dfs(rLast, c, currentLastRowHeight, vstAtl)
       
        # dfs in horizontal oceans starting left and rigth rows to dfs
        cFirst = 0
        cLast = cLength - 1
        for r in range(rLength):
            
            currentLeftColHeight = heights[r][cFirst]
            dfs(r, cFirst, currentLeftColHeight, vstPacific)
            
            currentRightColHeight = heights[r][cLast]
            dfs(r, cLast, currentRightColHeight, vstAtl)
        
        # find if which positions appear in both sets
        #print(vstPacific, vstAtl)        
        
        positionsReachedFromBothOceans = []
        for r, c in vstPacific:
            if((r,c) in vstAtl): 
                positionsReachedFromBothOceans.append([r,c])
                
        return positionsReachedFromBothOceans
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        