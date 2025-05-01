from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    coords = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                coords.setdefault(v, []).append((r, c))
    res = [row[:] for row in grid]
    # handle horizontal‐line values
    for v, pts in coords.items():
        rows = [r for r, _ in pts]
        cols = [c for _, c in pts]
        if len(pts) >= 2 and len(set(rows)) == 1:
            r0 = rows[0]
            l = len(cols)
            start = max(0, r0 - (l - 1))
            for r in range(start, r0 + 1):
                for c in sorted(cols):
                    if res[r][c] == 0:
                        res[r][c] = v
    # handle vertical stripes
    for v, pts in coords.items():
        if len(pts) >= 3 and len(set(r for r, _ in pts)) != 1:
            cols = sorted(c for _, c in pts)
            pivot = cols[len(cols) // 2]
            pivots = sorted(r for r, c in pts if c == pivot)
            if not pivots:
                pivots = sorted(r for r, _ in pts)
            prev = -1
            for r in pivots:
                for rr in range(prev + 1, r + 1):
                    if res[rr][pivot] == 0:
                        res[rr][pivot] = v
                prev = r
    return res