'''
Recursion:
f(5)
f(4)+f(3)
f(3)+f(2) + f(2)+f(1)
f(2)+f(1) + f(1)+f(0) + f(1)+f(0) 
f(1)+f(0)

Time complexity : O(2^N)
This is the slowest way to solve the Fibonacci, it takes exponential time. The amount of operations needed, for each level of recursion, 
grows exponentially as the depth approaches N. And also, the operations are repeated for each f() function opertaion.
Space complexity : O(N)
We need space proportionate to N to account for the max size of the stack, in memory. This stack keeps track of the function calls to fib(N).

'''
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)