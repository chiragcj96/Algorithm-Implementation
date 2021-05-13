'''
Using set data structure to determine all unique elements
Then find if the len of set and len of nums match
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        var = set(nums)
        return len(var)!=len(nums)
        '''
        return len(nums) != len(set(nums))
        '''

'''
Going through a sorted array and checking the previous ele equals the current, return True, otherwise False
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

