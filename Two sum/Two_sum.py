class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], i]
            hash[num] = i
        return []