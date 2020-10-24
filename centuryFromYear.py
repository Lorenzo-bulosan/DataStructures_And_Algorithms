
def centuryFromYear(year):
    ''' return century given a year
    '''
    
    #determine length of digits
    strYear = str(year)
    yearLength = len(strYear)
    
    # edge case 
    if (year < 101): 
        return 1
    
    # get century from digits
    yearWithoutLastTwoDigits = strYear[0:-2]
    
    #decide on the edge of century by looking at 4th digit
    if(int(strYear[-1]) == 0): 
        return int(yearWithoutLastTwoDigits) 
    
    century = int(yearWithoutLastTwoDigits) + 1
    
    return century