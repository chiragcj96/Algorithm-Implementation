class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i=1
        result=[]
        for i in range(1, n+1):
            if i==1 or i==2:
                result.append(str(i))
            elif i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%5==0:
                result.append("Buzz")
            elif i%3==0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result
                