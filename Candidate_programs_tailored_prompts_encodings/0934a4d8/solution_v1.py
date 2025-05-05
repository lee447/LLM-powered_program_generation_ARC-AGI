from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    eights = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 8]
    min_r = min(i for i, j in eights)
    max_r = max(i for i, j in eights)
    min_c = min(j for i, j in eights)
    max_c = max(j for i, j in eights)
    s = max_r - min_r + 1
    pr, pc = min_r - s, min_c - s
    return [row[pc:pc+s] for row in grid[pr:pr+s]]