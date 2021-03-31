class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        ""By applying mathematical formula and generating the integer back in reverse order""
        """
        result = 0                                      #The final result
        multiplier = 10                                 #to reconstruct the result from individually extracted digits
        isNegative = False                              #find if inout integer is negative, 
        if x<0:                                         #if negative, convert it to positive for further operations
            x = -1*x
            isNegative = True                           #Update isNegative Flag to true to reconvert to negative value
        while x !=0:
            result = (multiplier*result) + (x % 10)     #construct result by extracting each digit and adding it to the end
            x = x / 10                                  #update input x each time to remove last digit
        if isNegative == True:
            result = -1*result                          #if input was negtive, reconvert result to negative
        if result > (2**31-1) or result < (-2**31):     #if the final result is beyond the signed 32-bit integer range
            return 0
        return result