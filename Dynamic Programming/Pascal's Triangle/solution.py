'''
Dynamic Programming - 
matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

Using a list[list[]] is used to build a [numRows x numRows] matrix, initialized with all 1's
We then calculate each value for the pascal triangle by adding -> matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
This populates the whole matrix with correct values

Then we just run for all the levels of the triangles(0->numRows), then for each (x, numRows-x) pairs, we append the values to result
Return result

Time: O(N^2)
Space: O(N^2)
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [[1 for _ in range(numRows)] for _ in range(numRows)]
        result = []
    
        for i in range(1, numRows):
            for j in range(1, numRows):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        i = 0
        while i<numRows:
            temp = []
            x = 0
            while x<=i:
                temp.append(matrix[x][i-x])
                x += 1
            result.append(temp)
            i += 1
        return result
        