'''
But it is really time-intensive as we build temp and check everytime or else append to it
And also sort it beforehand
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        temp = []
        for i, num in enumerate(nums):
            if num+k in nums[i+1:] and [num+k, num] not in temp:
                count += 1
                temp.append([num+k, num])
        return count


'''
Enumerate is just to simplify notations of ith index array element
Same code but written as we commonly do -
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        temp = []
        for i in range(len(nums)):
            if nums[i]+k in nums[i+1:] and [nums[i]+k, nums[i]] not in temp:
                count += 1
                temp.append([nums[i]+k, nums[i]])
        return count
        