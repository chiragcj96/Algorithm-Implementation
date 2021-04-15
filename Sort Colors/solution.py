class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            nums[index] = num
            if num != 1:
                index += 1
        # nums[:len(nums) - index] = [0]*(len(nums) - index)
        nums[index:] = [1]*(len(nums) - index)
        index=0
        for num in nums:
            nums[index] = num
            if num != 2:
                index += 1
        # nums[:len(nums) - index] = [0]*(len(nums) - index)
        nums[index:] = [2]*(len(nums) - index)
        return
            
        