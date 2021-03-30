class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic_brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for bracket in s:
            if bracket in dic_brackets.values():
                stack.append(bracket)
                
            else: 
                if not stack:
                    return False
                if stack.pop() != dic_brackets[bracket]:
                    return False
                
        if len(stack) != 0:
            return False
        else:
            return True