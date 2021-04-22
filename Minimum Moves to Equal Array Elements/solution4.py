'''
Using Math
This approach is based on the idea that adding 1 to all the elements except one is equivalent to 
decrementing 1 from a single element, since we are interested in the relative levels. It is obvious 
that we'll reduce all the elements of the array to the minimum element. But, in order to find the solution, we 
need not actually decrement the elements. We can find the number of moves required as 
moves= ∑ {i=(0->n-1)} a[i]−min(a)∗n, where nn is the length of the array.
'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count+=nums[i]
        return count-min(nums)*len(nums)