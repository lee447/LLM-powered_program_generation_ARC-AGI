from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    eights = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 8]
    min_r = min(i for i, j in eights)
    max_r = max(i for i, j in eights)
    min_c = min(j for i, j in eights)
    max_c = max(j for i, j in eights)
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    best = None
    best_score = None
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            if i <= max_r and i + h - 1 >= min_r and j <= max_c and j + w - 1 >= min_c:
                continue
            vals = [grid[i + di][j + dj] for di in range(h) for dj in range(w)]
            if 8 in vals:
                continue
            score = sum(vals)
            if best is None or score < best_score:
                best = (i, j)
                best_score = score
    i0, j0 = best
    return [row[j0:j0 + w] for row in grid[i0:i0 + h]]