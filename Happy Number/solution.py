class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getSquared(n):              # we define a function which slices one digit at a time and
            sqSum = 0                   # adds it to the sqSum value
            while n > 0:
                digit = n%10
                sqSum += digit ** 2
                n = n/10
            return sqSum
    # Option1 (List)---------------------
        sqList = []                     # we use a storage data structure-store all sqSum values
        while n != 1 and n not in sqList:
            sqList.append(n)            # append sqSum value to sqList
            n = getSquared(n)
    # -----------------------------------
            
        return n==1                 # why do we return n==1 after both upper conditions don't pass
                                    # i.e. the sqSum reaches to 1

    '''
    # Option2 (HashSet)------------------
        sqList = set()                  # we use a storage data structure-store all sqSum values
        while n != 1 and n not in sqList:
            sqList.add(n)               # append sqSum value to sqList
            n = getSquared(n)
    # -----------------------------------
    '''