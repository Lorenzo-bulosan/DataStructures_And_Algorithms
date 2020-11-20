# sum of all elements where not 0 in last row
# [
#   [0 1 1]
#   [7 0 1]
#   [9 8 2]
# ]
# i.e sum = 5 as 7,8,9 are under 0s

def matrixElementsSum(matrix: list) -> int:
    ''' sums all elements of the matrix where it wasn't 0 in the last row
        In: int[][] matrix 
        Out: int sum of elements that fulfill the conditions
    '''
    # initialize needed variables
    indexesOfGhost = []
    totalSum = 0
    rowToSkip = 0
    
    # traverse the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            
            matrixElement = matrix[row][col]

            # skip the first row
            if(row==rowToSkip):                   
                totalSum = totalSum + matrixElement
                # get the indexes of 0s
                if(matrixElement == 0):
                    indexesOfGhost.append(col)
            
            # for the other rows
            else:          
                # if not ghost index sum
                if(not col in indexesOfGhost):
                    totalSum = totalSum + matrixElement
                
                # update ghost
                if(matrixElement == 0):
                    indexesOfGhost.append(col)
        # end of for
    # end of for
    
    return totalSum
