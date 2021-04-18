class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)             # Append zeroes to equalize number of digits
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):             # Start from the back of a and b
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2                         # carry = carry//2 only returns integer value of division
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)