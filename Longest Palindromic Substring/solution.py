'''
Intuitively, we list all the substrings, pick those palindromic, and get the longest one. However, that causes TLE 
for we reach the same situations (input substrings) many times.

To optimize, we decompose the problem as follows

for s = e, "a" is palindromic,
for s + 1 = e, "aa" is palindromic (if str[s] = str[e])
for s + 2 = e, "aba" is palindromic (if str[s] = str[e] and "b" is palindromic)
for s + 3 = e, "abba" is palindromic (if str[s] = str[e] and "bb" is palindromic)

we realize that
for s + dist = e, str[s, e] will be palindromic (if str[s] == str[e] and str[s + 1, e - 1] is palindromic)


Time complexity : O(n^2). 
Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
Space complexity : O(1).
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if(s=='' or len(s)<1):
        #     return ''
        result = ''
        for i in range(len(s)):
            tmp = self.expandAroundCenter(s, i, i)     #for odd len case like 'aba'
            if len(tmp) > len(result):
                result = tmp
            tmp = self.expandAroundCenter(s, i, i+1)   #for even len case like 'abba'
            if len(tmp) > len(result):
                result = tmp
        return result
    
    def expandAroundCenter(self, s, left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:       #L, R represent middle indexes
                left -= 1                                               #and stretch out to both ends
                right += 1
            return s[left+1:right]                             #return substring until s[L]==s[R] stands