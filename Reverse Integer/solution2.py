class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        ""By converting the integer to string and reversing it ""
        """
        isNegative = False                          #A flag to be used to reconvert to negative integer
        if x<0:
            x= -1*x                                 #converting negative input to positive for further operations
            isNegative = True
        x = str(x)  
        result = ""                                 #result stinrg definition                   
        for i in range(len(x)-1, -1, -1):           #iterating from the back side or reverse direction 
            result += x[i]                          #appending each string char(digit) to result
        result = int(result)                        #converting the string to integer
        if isNegative == True:
            result = -1*result                      #converting back to negative if isNegative flag is true
        if result > (2**31)-1 or result < (-2**31): #if beyond permissible range, return 0
            return 0
        return result