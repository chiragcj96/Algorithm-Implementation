class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        max_subarray = nums[0]
        current_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num, current_subarray+num)
            max_subarray = max(current_subarray, max_subarray)
        return max_subarray