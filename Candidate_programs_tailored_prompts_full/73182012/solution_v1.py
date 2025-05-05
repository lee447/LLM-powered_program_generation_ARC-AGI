from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = []
    cols = []
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != 0:
                rows.append(i)
                cols.append(j)
    if not rows:
        return []
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)
    block = [grid[i][min_c:max_c+1] for i in range(min_r, max_r+1)]
    h, w = max_r - min_r + 1, max_c - min_c + 1
    qh, qw = h // 2, w // 2
    return [r[:qw] for r in block[:qh]]