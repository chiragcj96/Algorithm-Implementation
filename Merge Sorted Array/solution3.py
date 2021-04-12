class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]= [1,2,3,0,0,0]
        :type m: int            3
        :type nums2: List[int]= [2,5,6]
        :type n: int            3
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)-1                       # length=6 or m+n 
        #length = m+n 
        while m > 0 and n > 0:                      # Run till the length goes to zero
            # print(nums1[m-1], nums2[n-1], length) 
            if nums1[m-1] >= nums2[n-1]:            # index = length-1, iterate through all eles comparing them
                nums1[length] = nums1[m-1]          # assign larger value to end of nums1
                m -= 1                              # decrease m by one
                length -= 1                         # decrease length by one
            else:       
                nums1[length] = nums2[n-1]          # assign larger value to end of nums1
                n -= 1                              # decrease n by one
                length -= 1                         # decrease length by one
        # print("nums1 updated", nums1)
        # print("n is", n)
        # print("m is", m)
        if n >= 0:                                  # When we exit out loop, update the remaining nums2 to nums1
            nums1[:n] = nums2[:n]                   # [5,8,9,0,0,0] -> [_,_,_,5,8,9]+[2,3,4] -> [2,3,4,5,8,9]
                
            
            