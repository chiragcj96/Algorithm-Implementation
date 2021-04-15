class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if k==0:                            #if k=0 then we dont want anything to be returned to the 
            return []                       # null list
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1   
        topKFrequentWords = [k for k, v in sorted(d.items(), key=lambda x:(-x[1], x[0]))]
        return topKFrequentWords[:k]