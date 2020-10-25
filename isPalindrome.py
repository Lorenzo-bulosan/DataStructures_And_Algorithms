# Singly-linked lists are already defined with this interface:

def isListPalindrome(l):
    
    head = l
    result = True
    record = []
    
    # find length  
    length = 0
    tmpHead = head
    while(tmpHead):
        length+=1
        tmpHead = tmpHead.next
    
    middle = length//2
    
    print('length is: ' + str(length) + ' so middle is ' + str(middle))

    # traverse list and record first half
    i = 0
    tempHead2 = head
    while(tempHead2):
        if (i<=middle):
            record.append(tempHead2.value)
        # update 
        tempHead2 = tempHead2.next
        i+=1
        
    print('original first half')
    print(record)
    
    #reverse array to later check against if palindrome
    checkAgainst = reverseArray(record)
    print('reversed first half')
    print(checkAgainst)
    
    # traverse again and when reach the 2nd half compare with 'record'
    count , j = 0 , 0
    while(head):
        
        print('still on first half: ' + str(head.value))
       
        #compare from 2nd half
        if(count>=middle):
            print('compare these two:')
            print([head.value,checkAgainst[j]])
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
    
    if(len(a)==1): return a
    
    while(left<right):
        a[left],a[right] = a[right],a[left]
        left+=1
        right-=1
        
    return a

#%% Create link list to test
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# populate list nodes
x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(2)
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










