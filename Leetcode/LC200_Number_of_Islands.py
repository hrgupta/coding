"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
"""
Solution:
Runtime: 140 ms, faster than 81.66% of Python3 online submissions for Number of Islands.
Memory Usage: 14.7 MB, less than 9.40% of Python3 online submissions for Number of Islands.

Explanation:
The core idea is to sink the adjacent islands already connected to an island. If water is found
nothing is to be done. This is achieved by doing a DFS for each adjacent node.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    self.dfs(grid, i, j)
                    count +=1
        return count
    
    def dfs(self, grid, i, j):
        # Prototypical DFS for a matrix
        if(i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]=='0'):
            return
        grid[i][j] = '0' # sinking the island
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
