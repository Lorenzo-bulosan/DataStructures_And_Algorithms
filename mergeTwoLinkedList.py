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
    
    while(True):
        
        # no more elements on both lists
        if(l1==None and l2==None):
            break
        
        # l1 exausted
        if(l1==None and l2!=None):
            mergedList.append(l2.value)
            l2 = l2.next

        # l2 exausted
        elif(l2==None and l1!=None):
            mergedList.append(l1.value)
            l1 = l1.next     
        
        # both list still contain elements
        else:    
            if(l1.value < l2.value):
                mergedList.append(l1.value)
                l1 = l1.next
            else:
                mergedList.append(l2.value)
                l2 = l2.next
      
    return mergedList
