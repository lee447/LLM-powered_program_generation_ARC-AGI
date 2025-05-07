from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    sep = next(j for j, v in enumerate(grid[0]) if v == 5)
    left = [row[:sep] for row in grid]
    right = [row[sep+1:] for row in grid]
    w = len(left[0])
    ok = True
    for i in range(h):
        for j in range(w):
            if (left[i][j] == 0) == (right[i][j] == 0):
                ok = False
                break
        if not ok:
            break
    if ok:
        out = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                out[i][j] = left[i][j] if left[i][j] != 0 else right[i][j]
        return out
    return left