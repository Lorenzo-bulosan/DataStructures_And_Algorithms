# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):

    num1str = ''
    num2str = ''
    output = []
        
    #traverse linkedlist and complete full form 
    while(a):
        strA = str(a.value)

        #pads 0 for full 4 digit
        if(len(strA)!=4):
            strA = '0'*(4-len(strA)) + strA 
        
        num1str = num1str + strA           
        a = a.next
        
    #traverse linkedlist and complete full form 
    while(b):
        strB = str(b.value)
        
        #pads 0 for full 4 digit
        if(len(strB)!=4):
            strB = '0'*(4-len(strB)) + strB 
        
        num2str = num2str + strB            
        b = b.next
        
    #add as integers
    answer = int(num1str)+int(num2str)
    strAnswer = str(answer)
    print(strAnswer)
    
    #slice from right to left by 4
    for i in range(len(strAnswer),0,-4):
        
        # while there's sets of 4 digits
        if(strAnswer[i-4:i]):
            output.append(strAnswer[i-4:i])
            
        #if reach the end and no 4 digits will give error
        else:    
            padding = '0'*(4-i)
            strAnswer = padding+strAnswer
            output.append(strAnswer[0:4])
    
    #convert to int as it also removes padding
    for i in range(len(output)):
        output[i] = int(output[i])

    #reverse array
    left,right = 0, len(output)-1
    while(left<right):
        output[left],output[right] = output[right],output[left]
        left+=1
        right-=1
    
    return output 