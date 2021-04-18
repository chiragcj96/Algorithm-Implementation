class Solution:
    def addBinary(self, a: str, b: str) -> str:
        counta = 0
        countb = 0
        decimala = 0
        decimalb = 0
        if a==0:
            return b
        elif b==0:
            return a
        
        a, b = int(a), int(b)
        
        while a!=0:                         # digit by digit we multiply by 2^power of digit and add to form decimal of a
            a, deca = divmod(a, 10)
            decimala += deca*2**counta 
            counta += 1
        print(decimala)
        
        while b!=0:                         # digit by digit we multiply by 2^power of digit and add to form decimal of b
            b, decb = divmod(b, 10)
            decimalb += decb*2**countb 
            countb += 1
        print(decimalb)
        
        result = decimala+decimalb          # decimal addition
        output = []
        while result!=1:
            result, rem = divmod(result, 2)
            output.insert(0, rem)
        output.insert(0, 1)                 # decimal to binary conversion of form [1,0,0] instead of 100

        s = [str(i) for i in output]
        res = "".join(s)                    # joining the elements to form a integer in string type
        return(res)
        
        # return output