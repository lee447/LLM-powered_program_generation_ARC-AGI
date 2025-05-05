from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    cols = sorted({j for j in range(len(grid[0])) if grid[0][j] == 2 or grid[1][j] == 2})
    n = len(cols)
    anchor_idx = n // 2
    anchor = cols[anchor_idx]
    clusters = [c for c in cols if c != anchor]
    w = len(clusters)
    out = [[0] * w for _ in range(w + 1)]
    curr = w // 2
    out[0][curr] = 3
    for i, c in enumerate(clusters):
        if c > anchor:
            curr += 1
        if grid[0][c] == 2 and grid[1][c] == 2:
            if curr + 1 < w:
                out[i + 1][curr] = out[i + 1][curr + 1] = 2
            else:
                out[i + 1][curr] = 2
        else:
            out[i + 1][curr] = 2
    return out