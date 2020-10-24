
def firstNotRepeatingCharacter(s):
    '''return first non-repeating character'''

    uniqueCharacters = {}
    
    for i in range(len(s)):
        
        # add to dictionary if it doesn't
        if s[i] not in uniqueCharacters:
            uniqueCharacters[s[i]] = True
        
        # flag that this is a repeated value
        elif s[i] in uniqueCharacters:
            uniqueCharacters[s[i]] = False
              
    # check for all duplicates
    for key, value in uniqueCharacters.items():
        if (value): return key
        
    return '_'