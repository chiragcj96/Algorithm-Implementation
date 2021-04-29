'''
We create a dict of all unique ele and their count
We then find that key with value greater or equal to len(nums)/2 and return the key

Time complexity : O(n). iterate over nums once and make a constant time HashMap insertion on each iteration. 
Space complexity : O(n) At most, the HashMap associations, so it occupies O(n)O(n) space.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic1 = {}
        for num in nums:
            dic1[num] = dic1.get(num, 0) + 1

        for i in range(len(list(dic1.values()))):
            if list(dic1.values())[i] >= len(nums)//2+1:
                return list(dic1.keys())[i]
            
#         ret =  (val >= n//2 for val in dic1.values())
#         return ret