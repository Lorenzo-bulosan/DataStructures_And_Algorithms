# e.g statues = [2,5,1]
# needs 3 and 4 to complete 1-5
# return number needed to complete i.e answer = 2

def makeArrayConsecutive2(statues: list) -> int:
    ''' method to find how many statues are needed to make consecutive numbers with diff = 1
        In: int[] statues
        out: int number of statues needed to complete it
    '''
    # determining largest statue
    largest = 0
    for i in range(len(statues)):
        if(statues[i]>largest):
            largest = statues[i]
    
    # determining smallest statue
    smallest = largest
    for i in range(len(statues)):
        if(statues[i]<smallest):
            smallest = statues[i] 
    
    print([smallest,largest])
            
    # figure out range needed
    rangeOfCompletedStatues = largest-smallest
    currentNumberOfStatues = len(statues)
    
    # needed to complete
    result = rangeOfCompletedStatues - currentNumberOfStatues + 1
    
    return result
