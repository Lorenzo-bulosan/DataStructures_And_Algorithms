# Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
#
# '/' is the root directory; the path should always start with it even if it isn't there in the given path;
# '/' is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory; this also means that // stands for "change the current directory to the current directory"
# '.' is used to mark the current directory;
# '..' is used to mark the parent directory; if the current directory is root #already, .. does nothing.
#
# e.g input = '/home/a/./x/../b//c/'
# ans = '/home/a/b/c'
#
def simplifyPath(path: str) -> str:
    ''' function to simplify a string of unix directory instructions
        In: str path of directory
        Out: str simplified directory
    '''
    
    if len(path) == 1: return path
    
    simplifiedString = []
    pathList = path.split('/')
    
    # add to results list according to conditions
    for char in pathList:
        
        # '' = double slash and '.' = /./
        if(char == '' or char == '.'): continue
        
        # remove last element if not root
        elif(char == '..'): 
            if(len(simplifiedString)==0): continue
            simplifiedString.pop()
        # keep the rest
        else:
            simplifiedString.append(char)
    
    # concatinate using a delimeter in between = a/b/c
    simplifiedString = '/'.join(simplifiedString)
    
    # add '/' to the start = /a/b/c
    simplifiedString = '/' + simplifiedString
    
    return simplifiedString
        
#%%
print(simplifyPath('/a/b//c/../l/../'))