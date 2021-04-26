'''
Directly use sorting and compare

Time Complexity: O(nlogn). n is the len(ss), sorting costs O(n log n) and comparing two strings costs O(n). So O(nlogn)
Space Complexity: O(1). Space depends on the sorting implementation which, usually, costs O(1) auxiliary space if 'heapsort' is used.
'''

class Solution:
    def isAnagram(self, ss: str, tt: str) -> bool:
        if len(ss)!=len(tt):
            return False
        ss = list(ss)
        tt = list(tt)
        ss.sort()
        tt.sort()
        # print(ss, tt)
        return ss==tt