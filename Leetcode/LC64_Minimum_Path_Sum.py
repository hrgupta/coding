'''Leetcode 30-day challenge
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
'''Solution
61 / 61 test cases passed.
Status: Accepted
Runtime: 192 ms
Memory Usage: 15.3 MB
'''
class Solution:
    def minPathSum(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        
        for i in range(1, nrows):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1, ncols):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, nrows):
            for j in range(1, ncols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[nrows-1][ncols-1]