from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep = next(j for j in range(w) if all(grid[i][j] == 5 for i in range(h)))
    lw, rw = sep, w - sep - 1
    m = min(lw, rw)
    left = [[grid[i][j] for j in range(m)] for i in range(h)]
    right = [[grid[i][j+sep+1] for j in range(m)] for i in range(h)]
    comp = all(left[i][j] != 0 or right[i][j] != 0 for i in range(h) for j in range(m))
    res = [[left[i][j] if not comp or left[i][j] != 0 else right[i][j] for j in range(m)] for i in range(h)]
    return res