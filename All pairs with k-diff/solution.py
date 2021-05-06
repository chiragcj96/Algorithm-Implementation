class Solution(object):
    def kDiffPair(self, nums, k):
        dic1 = {}
        result = []
        for i, num in enumerate(nums):
            temp = []
            dic1[num] = dic1.get(num, num+k)
            if dic1[num] in nums:
                temp.append(num)
                temp.append(dic1[num])
            if temp:
                result.append(temp) 
        return result