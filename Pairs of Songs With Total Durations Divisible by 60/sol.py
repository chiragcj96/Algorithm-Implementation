class Solution:
    def numPairsDivisibleBy60(self, time):
        c = [0] * 60
        res = 0
        for t in time:
            # print('c[-t % 60]', c[-t % 60])
            res += c[-t % 60]
            # print('res', res)
            c[t % 60] += 1
            # print('c[t % 60]', c[t % 60])
        return res

'''
Or
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, cnt = 0, collections.Counter()
        for t in time:
            theOther = -t % 60
            ans += cnt[theOther]
            cnt[t % 60] += 1
        return ans

'''
Or
Fastest and best memeory mgmt.
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = 0
        n = [0] * 60

        for i in time:
            n[i%60]+=1

        for i in range(0, 31):
            if n[i] == 0:
                continue
            if (i == 0 or i == 30):
                if n[i] > 1:
                    c+=(n[i]*(n[i]-1)/2)
            else:
                 c+=(n[i]*n[60-i])
        return int(c)