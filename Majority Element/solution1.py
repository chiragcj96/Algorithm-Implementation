'''
Here we use a counter 
First we sort the array and run the counter for all like eles. 
We update the counter if the ele changes and count till it sustains
When count hits len(nums), we return the result
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        count = 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                count += 1
            else:
                count = 1
            if count >= len(nums)//2+1:
                return nums[i]