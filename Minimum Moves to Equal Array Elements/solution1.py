'''
Brute force with sorting, here we sort the array, check diff(N[n-1], N[0]), if not equal, increment n-1 eles, count+1 and sort everytime
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        n=0
        i, j = 0, 0
        count = 0
        while i<1:
            if nums[n-1]!=nums[0]:
                for j in range(len(nums)-1):
                    nums[j]+=1
                count += 1
                nums.sort()
            else:
                i=1
        return count
        
            