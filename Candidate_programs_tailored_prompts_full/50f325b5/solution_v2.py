from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    eights = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 8]
    ref_r, ref_c = min(eights)
    offsets = [(r - ref_r, c - ref_c) for r, c in eights]
    anchors = [(r, c) for r in range(H) for c in range(W) if grid[r][c] in (2, 7)]
    out = [row[:] for row in grid]
    for ar, ac in anchors:
        for dr, dc in offsets:
            rr, cc = ar + dr, ac + dc
            if 0 <= rr < H and 0 <= cc < W:
                out[rr][cc] = 8
    return out