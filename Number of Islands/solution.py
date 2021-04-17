class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = []
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numIslands += 1
                    q = [(i,j)]
                    print("value of q", q)
                    self.bfs(grid, i, j, q)
                    
        return numIslands
        
    def bfs(self, grid, i, j, q):
        l = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            x, y = q.pop(0)
            print("x, y, q.pop", x, y)

            for dx, dy in l:
                print("dx, dy", dx, dy)
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[new_x]) or grid[new_x][new_y] == '0':
                    continue
                if grid[new_x][new_y] == '1':
                    grid[new_x][new_y] = '0'
                    q.append([new_x, new_y])
                print("final is the the ht q", q)
        