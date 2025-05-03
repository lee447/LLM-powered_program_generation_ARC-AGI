from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    sep_rows = sorted(r for r in range(rows) if all(grid[r][c] == 4 for c in range(cols)))
    sep_cols = sorted(c for c in range(cols) if all(grid[r][c] == 4 for r in range(rows)))
    sep_rows = [-1] + sep_rows + [rows]
    sep_cols = [-1] + sep_cols + [cols]
    h = sep_rows[1] - sep_rows[0] - 1
    w = sep_cols[1] - sep_cols[0] - 1
    motif_color = None
    motif = []
    for bi in range(len(sep_rows) - 1):
        for bj in range(len(sep_cols) - 1):
            r0 = sep_rows[bi] + 1
            c0 = sep_cols[bj] + 1
            colors = {grid[r0+dr][c0+dc] for dr in range(h) for dc in range(w) if grid[r0+dr][c0+dc] not in (0,1,4)}
            if colors:
                motif_color = colors.pop()
                motif = [(dr, dc) for dr in range(h) for dc in range(w) if grid[r0+dr][c0+dc] == motif_color]
                break
        if motif_color is not None:
            break
    res = [row[:] for row in grid]
    if motif_color is None:
        return res
    for bi in range(len(sep_rows) - 1):
        for bj in range(len(sep_cols) - 1):
            r0 = sep_rows[bi] + 1
            c0 = sep_cols[bj] + 1
            for dr, dc in motif:
                res[r0+dr][c0+dc] = motif_color
    return res