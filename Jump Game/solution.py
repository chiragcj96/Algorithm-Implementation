'''
Greedy approach-
Start from the last or right-most index, start iterating left towards first index
and keep checking if it can make your reach to the last element. 
Each time such an index is found, we update the last index to this, and reduce the problem area.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0