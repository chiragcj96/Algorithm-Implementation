class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Does work for few test cases but will reach Timeout due to 0(N^2) complexity
        It is Brute force which is optimized to N^2  complexity instead of the normal Brute Force with N^3 complexity
        """
        max_subarray = -float('inf')
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray