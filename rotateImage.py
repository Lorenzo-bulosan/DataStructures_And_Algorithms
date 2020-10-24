def rotateImage(a):
    '''
    Given a nxn matrix rotate 90degree to the right
    return the rotated matrix
    '''
    
    matrix = a
    matrixLength = len(matrix[0])
    tMatrix = matrix
    
    #transpose matrix
    for row in range(matrixLength):
        for column in range(row,matrixLength):
            tMatrix[column][row],tMatrix[row][column] = matrix[row][column],matrix[column][row]
            
    print(tMatrix)
    
    # use double pointer technique to reverse array
    leftPointer = 0
    rightPointer = matrixLength-1
    
    # reverse array in each row
    for row in range(matrixLength):
        
        leftPointer = 0
        rightPointer = matrixLength-1
        
        while(leftPointer<rightPointer):
            tMatrix[row][leftPointer],tMatrix[row][rightPointer] = tMatrix[row][rightPointer],tMatrix[row][leftPointer]
            leftPointer += 1
            rightPointer -=1
            
    out = tMatrix
    
    return out