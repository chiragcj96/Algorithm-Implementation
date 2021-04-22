'''
Using DP
            diff = count+nums[i]-nums[i-1]
            nums[i]+=count
            count += diff
Here we dont update/increment the elements and sort them everytime,
instead we save and update the diff of i to i-1, add it to count and increment nums[i] with count each time
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            diff = count+nums[i]-nums[i-1]
            nums[i]+=count
            count += diff
        return count