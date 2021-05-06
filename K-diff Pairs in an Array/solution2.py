'''
Hashmap
This method removes the need to sort the nums array. Rather than that, we will be building a frequency hash map. 
This hash map will have every unique number in nums as keys and the number of times each number shows up in nums as values.

For example:
nums = [2,4,1,3,5,3,1], k = 3
hash_map = {1: 2,
            2: 1,
            3: 2,
            4: 1,
            5: 1}

Time complexity : O(N)
It takes O(N) to create an initial frequency hash map and another O(N) to traverse the keys of that hash map. 
One thing to note about is the hash key lookup. The time complexity for hash key lookup is O(1)
but if there are hash key collisions, the time complexity will become O(N). 
However those cases are rare and thus, the amortized time complexity is O(2N)≈O(N).

Space complexity : O(N)
the maximum size of our table would be O(N).
'''


from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)
        print(counter)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result