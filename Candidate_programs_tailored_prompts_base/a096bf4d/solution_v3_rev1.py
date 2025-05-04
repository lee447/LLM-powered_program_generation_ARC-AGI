from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    black = 0
    sep_rows = [i for i in range(h) if all(grid[i][j] == black for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j] == black for i in range(h))]
    row_segs = [(sep_rows[i]+1, sep_rows[i+1]) for i in range(len(sep_rows)-1) if sep_rows[i]+1 < sep_rows[i+1]]
    col_segs = [(sep_cols[i]+1, sep_cols[i+1]) for i in range(len(sep_cols)-1) if sep_cols[i]+1 < sep_cols[i+1]]
    out = [row[:] for row in grid]
    for r0, r1 in row_segs:
        mid = r0 + (r1 - r0)//2
        patterns = [tuple(grid[mid][c0:c1]) for c0, c1 in col_segs]
        counts = {}
        for i,p in enumerate(patterns):
            if p not in counts:
                counts[p] = [0, i]
            counts[p][0] += 1
        best = None
        best_count = -1
        best_idx = len(patterns)
        for p,(cnt, idx) in counts.items():
            if cnt > best_count or (cnt == best_count and idx < best_idx):
                best_count, best_idx, best = cnt, idx, p
        for (c0, c1), pat in zip(col_segs, patterns):
            for dx in range(c1 - c0):
                out[mid][c0 + dx] = best[dx]
    return out