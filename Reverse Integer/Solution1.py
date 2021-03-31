class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        multiplier = 10
        Flag = False
        if x<0:
            x = -1*x
            Flag = True
        while x !=0:
            result = (multiplier*result) + (x % 10)
            # multiplier = multiplier*10
            x = x / 10
        if Flag == True:
            result = -1*result
        if result > (2**31-1) or result < (-2**31):
            return 0
        return result