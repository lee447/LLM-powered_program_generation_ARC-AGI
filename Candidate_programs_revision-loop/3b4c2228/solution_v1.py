from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    k = 0
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j] == 3 and grid[i+1][j+1] == 3:
                k += 1
    out = [[0]*3 for _ in range(3)]
    for i in range(min(k, 3)):
        out[i][i] = 1
    return out