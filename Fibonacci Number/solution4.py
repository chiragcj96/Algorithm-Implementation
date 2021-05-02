'''
Iterative Top-Down Approach - 
Let's get rid of the need to use all of that space and instead use the minimum amount of space required. 
We can achieve O(1)O(1) space complexity by only storing the value of the two previous numbers and updating them as we iterate to N.

Time complexity : O(N). Each value from 2 to N will be visited at least once.

Space complexity : O(1). This requires 1 unit of Space for the integer N and 3 units of Space to store the computed values (curr, prev1 and prev2) for every loop iteration. 
The amount of Space doesn't change so this is constant Space complexity.
'''
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current