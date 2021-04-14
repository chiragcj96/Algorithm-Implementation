class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        It is brute force method to first sort the arr with Bubble sort and then return Kth ele from end
        """
        self.bubble_sort(nums)
        return nums[-k]
    
    def bubble_sort(self, nums):
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if nums[i - 1] > nums[i]:
                    swap(i - 1, i)
                    swapped = True

        # return nums
        
        