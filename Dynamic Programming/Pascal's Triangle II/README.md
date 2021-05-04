# Pascal's Triangle

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

                    1
                1       1
            1       2       1
        1       3       3       1
    1       4       6       4       1   

### Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]

    Input: rowIndex = 0
    Output: [1]

    Input: rowIndex = 1
    Output: [1,1]

### Constraints:

- 0 <= numRows <= 33

### Further Thoughts:

- Could you optimize your algorithm to use only O(rowIndex) extra space?