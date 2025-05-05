from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    shape = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not shape:
        return [row[:] for row in grid]
    minr = min(r for r, c in shape)
    minc = min(c for r, c in shape)
    offsets = [(r - minr, c - minc) for r, c in shape]
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] in (2, 7)]
    out = [row[:] for row in grid]
    for ar, ac in anchors:
        dr = minr - ar
        dc = minc - ac
        coords = [(ar + dr + orf, ac + dc + ocf) for orf, ocf in offsets]
        valid = True
        for rr, cc in coords:
            if not (0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0):
                valid = False
                break
        if valid:
            for rr, cc in coords:
                out[rr][cc] = 8
    return out