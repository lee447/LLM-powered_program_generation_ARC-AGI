from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    anchors = []
    reds = []
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v == 4:
                anchors.append((r, c))
            elif v == 2:
                reds.append((r, c))
    # pick the anchor nearest to the red cluster (by sum of squared distances)
    best = None
    best_score = None
    for ar, ac in anchors:
        s = 0
        for rr, cc in reds:
            dr = rr - ar
            dc = cc - ac
            s += dr*dr + dc*dc
        if best_score is None or s < best_score or (s == best_score and (ar, ac) < best):
            best_score = s
            best = (ar, ac)
    ar0, ac0 = best
    offsets = [(rr - ar0, cc - ac0) for rr, cc in reds]
    out = [[0]*W for _ in range(H)]
    for ar, ac in anchors:
        for dr, dc in offsets:
            rr, cc = ar + dr, ac + dc
            if 0 <= rr < H and 0 <= cc < W and out[rr][cc] == 0:
                out[rr][cc] = 2
    for ar, ac in anchors:
        out[ar][ac] = 4
    return out