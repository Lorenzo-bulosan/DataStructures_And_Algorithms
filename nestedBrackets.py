# given a string of values=(){}[]
# return 1 if brackets are closed correctly
# e.g S='{([])}[]()' 
# ans = 1
#
def nestedBrackets(S: str) -> int:
    ''' function to verify if brackets are clossed correctly
        In: str input string of brackets
        Out: int return 1 if clossed properly otherwise 0
    '''
    
    # edge case: empty string
    if(len(S)==0): return 1

    # edge case: clossing bracket as first char
    char = S[0]
    if(char=='}' or char==']' or char==')'): return 0

    string = S
    stack = []

    for i in range(len(string)):
        
        char = string[i] 
        
        # add opening brackets to stack
        if(char=='{' or char=='[' or char=='('):
            stack.append(char)
        
        # detect clossing brackets
        elif(char=='}' or char==']' or char==')'):
            
            # edge case: no more opening only clossing
            if(len(stack)==0): return 0
            
            # when corresponding opposite bracket pop off the stack
            if(char=='}'):
                if(stack[-1]=='{'): 
                    stack.pop()
                    continue
                else: return 0
                
            elif(char==']'):
                if(stack[-1]=='['): 
                    stack.pop()
                    continue
                else: return 0
                
            elif(char==')'):
                if(stack[-1]=='('): 
                    stack.pop()
                    continue
                else: return 0
            
            # no match for opening brackets
            else: 
                return 0
    
    # if the stack not empty by this stage return 0
    if(len(stack)>0): return 0

    return 1

#%% Test
parenthesis = '([{}])[]'
out = nestedBrackets(parenthesis)
if(out==1): print('Test 1: passed')
else: print('Test 1: failed')

parenthesis = '{[()}'
out = nestedBrackets(parenthesis)
if(out==0): print('Test 2: passed')
else: print('Test 2: failed')

parenthesis = '()}}}}}'
out = nestedBrackets(parenthesis)
if(out==0): print('Test 3: passed')
else: print('Test 3: failed')

parenthesis = '}}}}}'
out = nestedBrackets(parenthesis)
if(out==0): print('Test 4: passed')
else: print('Test 4: failed')
