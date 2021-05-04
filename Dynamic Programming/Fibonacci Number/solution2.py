'''
Top-Down Approach using Memoization - 

Time complexity : O(N), Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.
Space complexity : O(N), The size of the data structure
'''
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        self.cache = {0: 0, 1: 1}

        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]

        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)

        return self.memoize(N)