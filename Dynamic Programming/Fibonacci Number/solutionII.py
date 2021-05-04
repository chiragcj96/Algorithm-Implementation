'''
Using golden ration
phi φ = {1 + sqrt(5)}/2 ≈ 1.6180339887....

Time complexity : O(1). Constant time complexity since we are using no loops or recursion and the time is based on the result of performing the calculation.

Space complexity : O(1). The space used is the space needed to create the variable to store the golden ratio formula.
'''
class Solution:
    def fib(self, N):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** N + 1) / 5 ** 0.5)