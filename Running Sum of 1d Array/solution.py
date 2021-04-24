'''
Here we use result[] array, count and i index. We append count each time after adding it with nums[i]
Time complexity = O(n)
Space = O(1) if we dont consider space occupied by result[]
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        count = 0
        i=0
        while i<len(nums):
            count += nums[i]
            # result.append(result[-1]+nums[i])
            result.append(count)
            i += 1
        return result

'''
Here we use result[] array, i index. We append result[i] each time after adding result[-1] and nums[i]
[1,2,3,4]
i   nums[i]     resutl
0   1           1
1   2           1+2=3
2   3           3+3=6
3   4           6+4=10
Hence we decreased one linear space usage
Time complexity = O(n)
Space = O(1) if we dont consider space occupied by result[]
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        i=1
        while i<len(nums):
            result.append(result[-1]+nums[i])
            i += 1
        return result

'''
Here, we do the operation in place, hence consuming even less linear space
Time complexity = O(n)
Space = O(1) if we dont consider space occupied by result[]
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i=1
        while i<len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums