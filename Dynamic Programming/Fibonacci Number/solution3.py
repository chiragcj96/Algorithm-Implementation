'''
'Bottom-Up Approach using Memoization (Using List DataStructure) - '
Time complexity : O(N), Each number, starting at 2 up to and including N, is visited, computed and then stored for O(N) access later on.
Space complexity : O(N), The size of the data structure
'''
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]

'''
'Bottom-Up Approach using Memoization (Using Dictionary DataStructure) - '
Time complexity : O(N), Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.
Space complexity : O(N), The size of the data structure
'''
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        cache = {0: 0, 1: 1}

        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]

'''
Time complexity : O(N), Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.
Space complexity : O(N), The size of the data structure
'''
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]