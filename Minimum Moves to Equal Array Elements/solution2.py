'''
We use maths here
for nums = [4, 9, 0, 7] we see that the #of moves required = (9-0)+(7-0)+(4-0) = 20

so we first sort the array and the count+ all the n-1 differences to lowest element
'''

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1, 0, -1):
            count += nums[i]-nums[0]
        return count
        