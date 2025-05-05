from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    anchors = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    reds = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    best = None
    best_score = None
    for ar, ac in anchors:
        s = sum(abs(rr-ar) + abs(cc-ac) for rr, cc in reds)
        if best_score is None or s < best_score:
            best_score = s
            best = (ar, ac)
    ar0, ac0 = best
    offsets = [(rr-ar0, cc-ac0) for rr, cc in reds]
    out = [[0]*W for _ in range(H)]
    for ar, ac in anchors:
        out[ar][ac] = 4
    for ar, ac in anchors:
        for dr, dc in offsets:
            rr, cc = ar+dr, ac+dc
            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] != 4:
                out[rr][cc] = 2
    return out