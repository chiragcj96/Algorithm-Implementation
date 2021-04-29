'''
It bases on the theory that after sorting, the majority element will be present in the middle index
Middle index can be eg: 5/2=2 or 6/2=3 indexed
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        nums.sort()
        return nums[len(nums)//2]