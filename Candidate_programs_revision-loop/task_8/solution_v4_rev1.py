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
    groups = {}
    for v, pts in coords.items():
        if len(pts) >= 3:
            cols = sorted(c for _, c in pts)
            pivot = cols[len(cols)//2]
            groups.setdefault(pivot, []).append(v)
    for pivot, vs in groups.items():
        vs.sort(key=lambda v: min(r for r, _ in coords[v]))
        prev_end = -1
        for v in vs:
            rows = [r for r, _ in coords[v]]
            end = max(rows)
            start = 0 if prev_end < 0 else prev_end + 1
            for r in range(start, end+1):
                if res[r][pivot] == 0:
                    res[r][pivot] = v
            prev_end = end
    return res