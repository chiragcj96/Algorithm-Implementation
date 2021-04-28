'''
Using one Dictinary
Increment by 1 if the key is found in s[i]
Decrement by 1 if the key is found in t[i]
return if all values of the dictionary are zero
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dic1 = {}

        for i in range(len(s)):
            dic1[s[i]] = dic1.get(s[i], 0) + 1
            dic1[t[i]] = dic1.get(t[i], 0) - 1
    # Option 1 ----------------------
        # for vals in dic1.values():
        #     if vals != 0:
        #         return False
        # return True
    # -------------------------------
    # Option 2 ----------------------
        return all(val == 0 for val in dic1.values())
    # -------------------------------

'''
Time complexity = More than other option as you loop through dic values
Space complexity = It will be better as only one dictionary is reqd

Time complexity : O(1). because accessing the dictionary is a constant time operation.
Space complexity : O(1). Although we do use extra space, the space complexity is O(1) because the dictionary's size stays constant no matter how large n is.
''' 

        