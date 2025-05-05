from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    count = 0
    for i in range(n-1):
        for j in range(m-1):
            if grid[i][j] == 3 and grid[i+1][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j+1] == 3:
                count += 1
    count = min(count, 3)
    out = [[0]*3 for _ in range(3)]
    for i in range(count):
        out[i][i] = 1
    return out