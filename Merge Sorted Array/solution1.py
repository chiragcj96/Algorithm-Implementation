class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        """
        This is a pythionic way, utilizing the python method sort() to implement code. Check solution2 for other way
        """
        nums1[m:] = nums2
        nums1.sort() 