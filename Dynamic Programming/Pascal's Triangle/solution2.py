'''
Dynamic Programming - 
Here, instead of a complete n*n matrix, we only use a triangle (or upper diagonal triangle of the n*n matrix)

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

which is 

1 1 1 1 1
1 2 3 4 .
1 3 6 . .
1 4 . . .
1 . . . .

And we return the values out

Time: O(N^2)
Space: O(N^2)
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle