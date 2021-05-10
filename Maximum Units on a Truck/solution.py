class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def takeSecond(elem):
            return elem[1]
        boxTypes.sort(key=takeSecond, reverse=True)
        
        count = 0
        for i in range(len(boxTypes)):
            while truckSize>0 and boxTypes[i][0]>0:
                count += boxTypes[i][1]
                truckSize -= 1
                boxTypes[i][0] -= 1
        return count


'''
Using Lambda function
'''

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                ans += box * units
            else:
                ans += truckSize * units
                return ans
        return ans 

        