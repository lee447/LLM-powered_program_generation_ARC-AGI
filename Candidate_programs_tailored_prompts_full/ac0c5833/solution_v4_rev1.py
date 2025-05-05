from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    anchors_r = sorted({r for r in range(rows) for c in range(cols) if grid[r][c] == 4})
    anchors_c = sorted({c for r in range(rows) for c in range(cols) if grid[r][c] == 4})
    reds = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2]
    if not reds:
        return grid
    rmin = min(r for r, c in reds)
    cmin = min(c for r, c in reds)
    base_r = max(r for r in anchors_r if r <= rmin)
    base_c = max(c for c in anchors_c if c <= cmin)
    pattern = [(r - base_r, c - base_c) for r, c in reds]
    out = [row[:] for row in grid]
    for ar in anchors_r:
        for ac in anchors_c:
            for dr, dc in pattern:
                r, c = ar + dr, ac + dc
                if 0 <= r < rows and 0 <= c < cols and out[r][c] == 0:
                    out[r][c] = 2
    return out