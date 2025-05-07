from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    best = (0, 0, 0, 0, 0)
    for i0 in range(h):
        for j0 in range(w):
            if grid[i0][j0] == 0:
                continue
            for i1 in range(i0 + 1, h):
                for j1 in range(j0 + 1, w):
                    area = (i1 - i0 + 1) * (j1 - j0 + 1)
                    if area <= best[0]:
                        continue
                    colors = set()
                    ok = True
                    for i in range(i0, i1 + 1):
                        for j in range(j0, j1 + 1):
                            v = grid[i][j]
                            if v == 0:
                                ok = False
                                break
                            colors.add(v)
                            if len(colors) > 2:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok and len(colors) == 2:
                        best = (area, i0, j0, i1, j1)
    _, r0, c0, r1, c1 = best
    H, W = r1 - r0 + 1, c1 - c0 + 1
    P = [grid[i][c0:c0+W] for i in range(r0, r0+H)]
    out = [row[:] for row in grid]
    pattern_cols = set(P[i][j] for i in range(H) for j in range(W))
    offsets = [(0, W), (H, 0), (H, W)]
    for dr, dc in offsets:
        sr, sc = r0 + dr, c0 + dc
        if sr < 0 or sc < 0 or sr + H > h or sc + W > w:
            continue
        hint_vals = set()
        mapping = {}
        for i in range(H):
            for j in range(W):
                v = grid[sr + i][sc + j]
                if v != 0 and v not in pattern_cols:
                    hint_vals.add(v)
                    orig = P[i][j]
                    mapping[orig] = v
        rem_orig = sorted(pattern_cols - mapping.keys())
        rem_vals = sorted(hint_vals - set(mapping.values()))
        if len(rem_orig) == 1 and len(rem_vals) == 1:
            mapping[rem_orig[0]] = rem_vals[0]
        for i in range(H):
            for j in range(W):
                if out[sr + i][sc + j] == 0:
                    out[sr + i][sc + j] = mapping.get(P[i][j], 0)
    return out