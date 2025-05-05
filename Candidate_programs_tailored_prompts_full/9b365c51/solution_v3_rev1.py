from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    stripes = []
    for c in range(W):
        for r in range(H):
            v = grid[r][c]
            if v not in (0, 8):
                stripes.append((c, v))
                break
    stripes.sort()
    colors = [v for _, v in stripes]
    blank_cols = []
    col_ranges = {}
    for c in range(W):
        rows = [r for r in range(H) if grid[r][c] == 8]
        if rows:
            col_ranges[c] = (min(rows), max(rows))
            blank_cols.append(c)
    blank_cols.sort()
    clusters = []
    prev_c = None
    prev_rng = None
    for c in blank_cols:
        rng = col_ranges[c]
        if prev_c is None or c != prev_c + 1 or rng != prev_rng:
            clusters.append([c, c, rng])
        else:
            clusters[-1][1] = c
        prev_c, prev_rng = c, rng
    clusters.sort(key=lambda x: x[0])
    out = [[0]*W for _ in range(H)]
    for (start, end, (r0, r1)), color in zip(clusters, colors):
        for r in range(r0, r1+1):
            for c in range(start, end+1):
                if grid[r][c] == 8:
                    out[r][c] = color
    return out