class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Here, 
        time complexity - O(n)
        Space complexity - O(2) or O(1) for i and temp
        """
        temp = 0
        i=0
        while i<len(s)//2:
            print(i)
            # option 1 ----
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp
            # -------------
            # Option 2 ----
            # s[i], s[-i-1] = s[-i-1], s[i]
            # -------------
            i+=1
        return s
        
        