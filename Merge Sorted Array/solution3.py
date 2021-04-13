class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2

        self.bubble_sort(nums1)
        # return nums1

    def bubble_sort(self, nums1):
        def swap(i, j):
            nums1[i], nums1[j] = nums1[j], nums1[i]

        n = len(nums1)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if nums1[i - 1] > nums1[i]:
                    swap(i - 1, i)
                    swapped = True

        return nums1
                
            
            