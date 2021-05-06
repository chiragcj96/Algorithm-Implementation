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
        