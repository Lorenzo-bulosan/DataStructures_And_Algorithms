# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):

    # edgecase: no valid list
    if(l1==None and l2==None): return []
    
    # edge case: only one valid list
    if(l1==None and l2!=None): return l2
    if(l2==None and l1!=None): return l1

    
    mergedList = []
    
    while(l1):
        
        if(l1.value < l2.value):
            mergedList.append(l1.value)
            print(mergedList)
            l1 = l1.next
        else:
            mergedList.append(l2.value)
            print(mergedList)
            l2 = l2.next
    
            
    return mergedList
