'''
This is a fibonacci problem, here 'a' denotes all the fibonacci numbers and the number of ways the stairs can be climbed
n   a   b
---------
1   1   1
2   2   3
3   3   5
4   5   8
5   8   13
.
.
.

'''
### 1
class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):      # _ is that we dont care what we are iteratin, we only want the loop to run n times for some operation
            a, b = b, a + b
        return a

### 2
# Top down + memorization (dictionary)  
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:    
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

### 3
# Top down + memorization (list)
def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in xrange(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n-1, dic)
    
def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
    return dic[n]
        
### 4        
# Bottom up, O(n) space
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in xrange(n)]
    res[0], res[1] = 1, 2
    for i in xrange(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

### 5
# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in xrange(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b