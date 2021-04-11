class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        print(self.stack)
        popped= self.stack[-1]
        self.stack.pop()
        print(self.stack)
        return popped
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.stack)
        

    def popMax(self):
        """
        :rtype: int
        """
        # print("1", self.stack)
        self.stack.reverse()
        # print("2", self.stack)
        maxValue = max(self.stack)
        
        self.stack.remove(maxValue)
        self.stack.reverse()
        # print("3",self.stack)
        return maxValue


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()