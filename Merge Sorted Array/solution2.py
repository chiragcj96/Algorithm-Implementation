"""
The algo is to check each ele with its next ele and swap if not ascending
We use Recursion for iterating through all eles repeatedly until fully sorted
We use "flag" as the stopping point as and when we find flag=0, we stop recursing

""Bubble Sort""

--Start first recursion
2,3,7,4,6,5
2,3,4,7,6,5
2,3,4,6,7,5     __ended first
--Start second recursion
2,3,4,6,5,7
2,3,4,5,6,7     __ended second
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        flag = 1
        nums1[m:] = nums2                           #merging the two arrays

        print("nums1 after initial merge", nums1)

        self.sortArray(nums1, flag)                 # calling the function to start with first iteration
        return nums1, flag
    
    def sortArray(self, nums1, flag):
        print("\ninput nums", nums1, "flag", flag)
        if flag!=0:                                 # flag=1 means we have to sort further as atleast one neighbour couple weren't ascending
            flag = 0                                # reinitialize with flag=0
            print("flag reinitialized")
            for i in range(len(nums1)-1):
                print("nums1[i+1]:", nums1[i+1], "nums1[i]:", nums1[i])     #checking the neighbour couple 
                if nums1[i+1] < nums1[i]:
                    nums1[i], nums1[i+1] = nums1[i+1], nums1[i]             # swap values
                    flag = 1                                                # if not ascending, flag=1 and re-recurse
                print ("updated nums1", nums1)

            self.sortArray(nums1, flag)        