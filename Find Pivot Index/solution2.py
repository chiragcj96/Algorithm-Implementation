'''
Here we maintain two variables
leftSum = sum of left side for index i
rightSum = sum of right side for index i

And we update them each time we iterate to next index.
As soon as we find equal sums, we return the index.


'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i, leftSum = 0, -nums[0]
        rightSum = sum(num for num in nums)
        
        for i in range(len(nums)):
            leftSum += nums[(i-1 if i-1>-1 else 0)]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        return -1
            
        