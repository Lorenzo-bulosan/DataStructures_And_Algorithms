
def firstDuplicate(a):
    ''' find first duplicate in an array'''
    
    array = a
    record = {}
    duplicate = False
    
    for i in range(len(array)):
        
        # if not in record add new value
        if array[i] not in record:
            record[array[i]] = 1
        
        # if already exist in record add 1
        elif array[i] in record: 
            duplicate = True
            return array[i]
        
    if (duplicate == False): return -1
