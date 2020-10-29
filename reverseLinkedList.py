# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseList(a):
    ''' Input: reference head of linked list
        Output: reference head of reversed list
    '''
    
    previous = None
    current = a

    while(current):
        nextNode = current.next
        current.next = previous
        
        #update both
        previous = current
        current = nextNode
    
    return previous

#%% Create link list to test
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# populate list nodes
x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)
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
out = reverseList(x)
resultList = []

while(out):
    resultList.append(out.value)
    out = out.next
print('Output was:')
print(resultList)