# contains duplicate 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Two- sum

def twoSum(self, nums: List[int], target: int) -> List[int]:
    check = {}

    for index,value in enumerate(nums):
        diff = target - value
        if diff in check:
            return [check[diff],index]
        check[value] = index
    

    #This is O(n) time complexity