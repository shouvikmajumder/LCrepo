# contains duplicate 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def hasDuplicate(self, nums: List[int]) -> bool:
    check = []
    
    for i in nums: 
        if i not in check:
            check.append(i)
        elif i in check: 
            return True 
    return False

    #This is O(n) time complexity