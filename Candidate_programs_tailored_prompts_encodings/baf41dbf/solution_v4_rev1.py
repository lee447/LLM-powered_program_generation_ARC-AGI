from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    anchors = []
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v == 6:
                anchors.append((r, c))
            elif v == 3:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    new_min_r, new_max_r = min_r, max_r
    new_min_c, new_max_c = min_c, max_c
    for ar, ac in anchors:
        if ac < min_c:
            new_min_c = min(new_min_c, ac + 1)
        if ac > max_c:
            new_max_c = max(new_max_c, ac - 1)
        if ar < min_r:
            new_min_r = min(new_min_r, ar + 1)
        if ar > max_r:
            new_max_r = max(new_max_r, ar - 1)
    out = [[grid[r][c] if grid[r][c] in (3, 6) else 0 for c in range(cols)] for r in range(rows)]
    for c in range(new_min_c, new_max_c + 1):
        if out[new_min_r][c] != 6:
            out[new_min_r][c] = 3
        if out[new_max_r][c] != 6:
            out[new_max_r][c] = 3
    for r in range(new_min_r, new_max_r + 1):
        if out[r][new_min_c] != 6:
            out[r][new_min_c] = 3
        if out[r][new_max_c] != 6:
            out[r][new_max_c] = 3
    return out