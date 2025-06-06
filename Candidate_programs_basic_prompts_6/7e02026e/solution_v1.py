from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j]==0 and grid[i-1][j]==0 and grid[i+1][j]==0 and grid[i][j-1]==0 and grid[i][j+1]==0:
                for di,dj in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
                    res[i+di][j+dj] = 3
    return res