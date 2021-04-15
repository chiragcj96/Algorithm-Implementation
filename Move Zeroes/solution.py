class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        nums = [0,1,0,3,12]
        consider pulling out all zeroes from the list and shifting remaining eles to left
        [1,3,12,_,_]
        [0,0]
        Then we put back the zeroes by counting them and replacing them to end of list
        [1,3,12,0,0]
        """
        index = 0
        for num in nums:
            nums[index] = num                       # define the nums[index] to be num
            if num != 0:                            # if num is not zero, we uncrease the index (iterate to next), otherwise we update the nums[index] value with same index to the next num
                index += 1
        nums[index:] = [0]*(len(nums) - index)
        return
