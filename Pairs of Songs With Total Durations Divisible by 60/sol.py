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