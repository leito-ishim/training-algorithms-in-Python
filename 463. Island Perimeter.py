# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

def islandPerimeter(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                temp = 0
                if i == 0 or grid[i - 1][j] != 1:
                    temp += 1
                if i == len(grid) - 1 or grid[i + 1][j] != 1:
                    temp += 1
                if j == 0 or grid[i][j - 1] != 1:
                    temp += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] != 1:
                    temp += 1
                total += temp
    return total


print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(islandPerimeter([[1]]))
