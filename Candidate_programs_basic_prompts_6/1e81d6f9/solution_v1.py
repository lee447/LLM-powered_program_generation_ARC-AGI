from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    col_count = {}
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5:
                col_count[j] = col_count.get(j, 0) + 1
    stripe_col = max(col_count, key=col_count.get)
    left = set()
    right = set()
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v and v != 5:
                if j < stripe_col:
                    left.add(v)
                else:
                    right.add(v)
    candidates = [v for v in left & right if v > 1]
    if candidates:
        c = min(candidates)
        res = [[(0 if (j >= stripe_col and grid[i][j] == c) else grid[i][j]) for j in range(w)] for i in range(h)]
    else:
        res = [row[:] for row in grid]
    return res