'''
'''
class Solution:
    def fib(self, n: int) -> int:
        memoize = [-1 for x in range(n+1)]
        return self.calculateFibonacciRecur(memoize, n)
    
    def calculateFibonacciRecur(self, memoize, n):
        if n < 2:
            return n
        if memoize[n] >= 0:
            return memoize[n]

        memoize[n] = self.calculateFibonacciRecur(memoize, n - 1) + self.calculateFibonacciRecur(memoize, n - 2)
        return memoize[n]