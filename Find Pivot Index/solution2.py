'''
Here we maintain two variables
leftSum = sum of left side for index i
rightSum = sum of right side for index i

And we update them each time we iterate to next index.
As soon as we find equal sums, we return the index.

Time Complexity: O(N), where N is the length of nums.
Space Complexity: O(1), the space used by leftsum and S.

'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
            
        