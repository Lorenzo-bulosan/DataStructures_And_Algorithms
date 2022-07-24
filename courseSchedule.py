'''
solution for leetcode question 207
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # create adj list
        adjList = {}
        
        # init list with empty []
        for i in range(numCourses):
            adjList[i] = []
            
        # fill up adj list
        for first, last in prerequisites: # always size 2 it says on instructions
            adjList[first].append(last)
                  
        # dfs, return false if find in visited list
        vst = set() # visited nodes
        
        def dfs(n):
            
            if(n in vst): return False            
            if (adjList[n] == []): return True   
            
            vst.add(n)
            for i in adjList[n]:
                if( dfs(i) == False): return False
            
            # don't visit again
            adjList[n] = []
            vst.remove(n)
            
            return True
        
        # run for all courses
        for i in range(numCourses):
            if dfs(i) == False: return False
        
        return True