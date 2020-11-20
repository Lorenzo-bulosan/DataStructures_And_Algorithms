# given minutes e.g n=40
# return sum of digits in its hh:mm format
# e.g given n=90 => hh:mm=01:30 => answer=4  
#
def lateRide(n: int) -> int:
    ''' function to convert mins to hours format hh:mm and add all digits
        In: int minutes
        Out: int sum of all digits of hh:mm
    '''
    def hoursToFormat_hhmm(hours: float) -> str:
        ''' helper method to convert hours into hh:mm
            In: float hours e.g 1.5h
            Our: str in format hh:mm e.g '0000'
        '''
        # keep 2 decimals only
        hourFloat = round(hours,2) 
        
        # separate by decimal
        strHourFloat = str(hourFloat)
        subComponents = strHourFloat.split('.')
        strHour = subComponents[0]
        strMin = subComponents[1]
        
        # convert the remaining min from hour to min
        minutes = int(strMin) * 6   # not x60 because we lost decimal so its not 0.12*60 its 12*6
        
        # if minutes have 'decimals' too
        if(len(str(minutes))>2):  
            minutes = round(minutes,-1) # round to have only 2
            
        return strHour + str(minutes)
        
    # edge case: n=0
    if(n==0): return 0
    
    # edge case: less than 1h passed
    if(n<60):
        minutes = str(n)
        totalSum = 0
        for i in minutes:
            totalSum += int(i)   
        
        return totalSum
    
    # convert min to hour
    hourFloat = n/60

    # helper function
    strAllDigits = hoursToFormat_hhmm(hourFloat)

    # add all digits toguether
    totalSum = 0
    allDigits = strAllDigits
    for i in allDigits:
        totalSum += int(i)
    
    return totalSum

