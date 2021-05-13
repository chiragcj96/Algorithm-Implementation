'''Time Limit Exceeded '''
'''We check each elelment with its [1,k]th distant ele, return true if found equal any time, else False'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            temp = min(k,len(nums)-i-1)
            dist = 1
            while dist<=temp:
                if nums[i]==nums[i+dist]:
                    return True
                dist += 1
        return False

'''
Hash Table
Here we use a dictionary and store ele as key and index i as value
If the ele is found in dic and index of current to the found ele is less than equals to k, we return True
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        print(dic)
        return False
            
'''
Using set and working similar to above '''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                print(i-k)
                seen.remove(nums[i - k])
        return False
            
