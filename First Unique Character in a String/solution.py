'''
Use dict to store all uniques chars with count of frequency
return a list of keys and values and use only that char with val==1
return index of that char and use it in str s to return the index
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = {}
        index=0
        for i in range(len(s)):
            uniques[s[i]]=uniques.get(s[i], 0) + 1
        k = list(uniques.keys())
        val = list(uniques.values())
        print(k, val)
        if 1 in val:
            index = val.index(1)
        else:
            return -1
        return s.index(k[index])