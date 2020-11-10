#                E
#           /         \
#          E           D
#        /   \        /  \
#       E     D      D    E
#      / \   / \    / \   / \
#     E   D D   E  D   E E   D


# Solution cannot make the symmetric tree and traverse
# Need to know Thue-Morse Sequence

# from left to right pos as 0-n
# convert the pos to binary eg. pos 4 = 0100 = E
# count the number of 1s in the binary representation of the position
# notice that if the count(1) is even then is always Engineer/ odd=Doctor

#%% Solution in logic
def findProfession(level, pos):
   
    #edge case: first pos always Engineer
    if(pos==0):
        return 'Engineer' 
    
    # convert position to binary
    binaryPos = bin(pos-1) #important -1 because position starting 1 not 0
    
    # convert to string
    strPos = str(binaryPos)
    
    # count 1's
    count = 0
    for i in strPos:
        if(i=='1'):
            count+=1
    
    print(count)
        
    # when even = engineer
    if(count%2==0):
        return 'Engineer'
    else:
        return 'Doctor'