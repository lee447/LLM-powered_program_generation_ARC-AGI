from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    c = next(grid[i][j] for i in range(h) for j in range(w) if grid[i][j] != 0)
    m = {8: 2, 3: 1, 5: 4}
    f = m[c]
    return [[0 if grid[i][j] == c else f for j in range(w)] for i in range(h)]