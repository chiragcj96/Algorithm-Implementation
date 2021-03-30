class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        length = len(x)
        
        for i in range(length//2):
            if x[i] != x[-i-1]:
                return False 
        return True