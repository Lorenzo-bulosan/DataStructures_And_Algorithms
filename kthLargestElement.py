def kthLargestElement(nums: list, k: int) -> int:
    '''
    '''
    # edge case: empty list
    if(len(nums) == 0): return None
    
    # edge case: intput k
    if(k == None): return None
    
    # edge case: asking for element out of range
    if(k > len(nums)): return None
    
    sortedNums = sortingFunction(nums)
    
    return sortedNums[len(nums)-k]
            
def sortingFunction(nums: list) -> list:
    '''
    '''
    nums.sort()
    return nums

#%% Test
nums = [1,4,6,3]
k = 1
klargest = kthLargestElement(nums, k)
print(klargest)