# You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

# Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
# Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
# Return true if all the cells satisfy these conditions, otherwise, return false.
# Input: grid = [[1,0,2],[1,0,2]]

# Output: true

# Input: grid = [[1,1,1],[0,0,0]]

# Output: false

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        a=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])-1):
                if(i!=(len(grid)-1)):
                    if grid[i][j] == grid[i+1][j] and grid[i][j] != grid[i][j+1]:
                        a.append(1)
                    else:
                        a.append(0)
                    count+=1
                elif(i==(len(grid)-1)):
                    if grid[i][j] != grid[i][j+1]:
                        a.append(1)
                    else:
                        a.append(0)
                    count+=1
            if i < len(grid) - 1:
                if grid[i][-1] == grid[i + 1][-1]:
                    a.append(1)
                else:
                    a.append(0)
                count += 1
        if sum(a)==count:
            return True
        return False
        
# ---------------------------------
#checking in reverse

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[i])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i < len(grid) - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                if j < len(grid[i]) - 1 and grid[i][j] == grid[i][j + 1]:
                    return False

        return True