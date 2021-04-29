'''
It bases on the theory that after sorting, the majority element will be present in the middle index
Middle index can be eg: 5/2=2 or 6/2=3 indexed

Time complexity : O(nlgn)

Sorting the array costs O(nlgn)O(nlgn) time in Python and Java, so it dominates the overall runtime.

Space complexity : O(1) or O(n)

We sorted nums in place here - if that is not allowed, then we must spend linear additional space on a copy of nums and sort the copy instead.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        nums.sort()
        return nums[len(nums)//2]