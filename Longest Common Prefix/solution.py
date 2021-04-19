class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        # for j in range(min(len(strs[0]), len(strs[1]))):
        #     if strs[0][j] == strs[1][j]:
        #         prefix.append(strs[0][j])
        #     else:
        #         pass
        prefix = strs[0]
        i = 1
        temp = []
        for i in range(len(strs)):
            for j in range(min(len(prefix), len(strs[i]))):
                if prefix[j] == strs[i][j]:
                    temp.append(strs[i][j])
                else:
                    break
            prefix = temp
            temp = []
        
        prefix = ''.join(prefix)
        return prefix
        