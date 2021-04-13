class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        This is   ** PYTHONIC **   way of doing it with sort() method
        """
        nums.sort()
        print(nums)
        return nums[-k]
        