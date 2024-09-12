# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.




# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4





class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    p = 4
                    # if we have a land above we have to subtract two edges
                    # 1st will be of above's land and second will be of curr land
                    if 0<=i-1 and grid[i-1][j]==1:
                        p -= 2
                    # if we have a land to left we have to subtact 2edges
                    # 1st is left connected edge and 2nd wwill be cuur land connectd with left land
                    if j-1>=0 and grid[i][j-1]==1:
                        p -= 2
                    ans += p
        return ans