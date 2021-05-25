class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        output = []
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1>=0 or p2>=0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            output.append(value)
            print(value, carry, output)
            p1 -= 1
            p2 -= 1
        
        if carry:
            output.append(carry)
            
        return str(output[::-1])