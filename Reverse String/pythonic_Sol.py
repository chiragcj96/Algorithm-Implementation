class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # return s[::-1]        # not in place, it just creates a copy of the string
        return s.reverse()      # this is in place
        # return reversed(s)    # not in place, this also creates a copy