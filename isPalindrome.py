# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

'''
Basic idea is to find the length
determine if its even or not to handle later
traverse through linked list and copy the 1st half
reverse the first half
traverse trough the linked list again and check against reverse half
'''
def isListPalindrome(l):
    ''' Accepts: linked list
        Returns: bool
    '''
    head = l
    result = True
    record = []
    
    # find length  
    length = 0
    tmpHead = head #important
    while(tmpHead):
        length+=1
        tmpHead = tmpHead.next
    
    # check if lenght list odd or even
    if(length%2==0):
        middle = length//2
        middle -= 1
        even = True
    else:
        middle = length//2
        even = False
    
    #print('length is: ' + str(length) + ' so middle is ' + str(middle))

    # traverse list and record first half
    i = 0
    tempHead2 = head #important
    while(tempHead2):
        if (i<=middle):
            record.append(tempHead2.value)
        # update 
        tempHead2 = tempHead2.next
        i+=1
    
    #reverse array to later check against if palindrome
    checkAgainst = reverseArray(record)
    
    #print(record)
    #print(checkAgainst)
    
    #traverse again and when reach the 2nd half compare with reversed half
    count = 0 #to keep track of position
    j = 0     #to iterate over 2nd half
    
    while(head):

        # if length even skip middle
        if(even):
            #compare from 2nd half
            if(count>middle):
                if(head.value != checkAgainst[j]):
                    return False
                j+=1
                
        # handle odd length
        else:
            #compare from 2nd half
            if(count>=middle):
                if(head.value != checkAgainst[j]):
                    return False
                j+=1
            
        #update
        head = head.next
        count+=1
        
    return result
    
def reverseArray(a):
    
    left=0
    right=len(a)-1
    
    # check if only one node
    if(len(a)==1): return a
    
    # double pointer to reverse
    while(left<right):
        a[left],a[right] = a[right],a[left]
        left+=1
        right-=1
        
    return a


'''
ALTERNATIVE SOLUTION
but uses internal function to reverse
'''
def isListPalindrome2(l):
    
    record = []
    
    while(l):
        record.append(l.value)
        l = l.next

    reverse = record[::-1]
    
    if(record == reverse):
        return True
        
    return False

#%% Create link list to test
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# populate list nodes
x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(2)
x.next.next.next = ListNode(1)
#x.next.next.next.next = ListNode(1)

# Check linked list values
testList = []
temp = x
while(temp):
    testList.append(temp.value)
    temp = temp.next
print('Testing with:')
print(testList)

# Test function
out = isListPalindrome(x)
print(out)










