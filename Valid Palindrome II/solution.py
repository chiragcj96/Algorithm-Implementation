class Solution:
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j)) #return true if all the conditions are true

        for i in range(len(s) // 2):
            if s[i] != s[~i]:                                 # (i, ~i) = (0, -1), (1,-2), (2,-3)...(i,-i-1)
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True