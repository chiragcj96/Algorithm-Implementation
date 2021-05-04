'''
Dynamic Programming - 
Here, instead of a complete n*n matrix, we only use a triangle (or upper diagonal triangle of the n*n matrix)

1                           (0,0)
1 1                     (1,0)   (1,1)
1 2 1               (2,0)   (2,1)   (2,2)
1 3 3 1         (3,0)   (3,1)   (3,2)   (3,3)
1 4 6 4 1   (4,0)   (4,1)   (4,2)   (4,3)   (4,4)

                                1
                            1       1
                        1       2       1
                    1       3       3       1
                1       4       6       4       1   

And we return the values out at the rowIndex provided.
Time: O(N^2)
Space: O(N^2)

'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        
        for rowNumber in range(rowIndex+1):
            row = [None for _ in range(rowNumber+1)]
            row[0], row[-1] = 1,1
            
            for j in range(1,len(row)-1):
                row[j] = triangle[rowNumber-1][j-1]+triangle[rowNumber-1][j]
                
            triangle.append(row)
            
        return triangle[rowIndex]