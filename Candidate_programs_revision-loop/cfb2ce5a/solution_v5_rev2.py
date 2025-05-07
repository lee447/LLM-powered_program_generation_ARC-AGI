from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    best = (0, 0, 0, 0, 0)
    for i0 in range(h):
        for j0 in range(w):
            if grid[i0][j0] == 0:
                continue
            for i1 in range(i0, h):
                for j1 in range(j0, w):
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
    def rot_cw(A):
        return [[A[H-1-j][i] for j in range(W)] for i in range(H)]
    def rot_ccw(A):
        return [[A[j][W-1-i] for j in range(W)] for i in range(H)]
    def rot_180(A):
        return [[A[H-1-i][W-1-j] for j in range(W)] for i in range(H)]
    transforms = [(0, W, rot_cw(P)), (H, 0, rot_ccw(P)), (H, W, rot_180(P))]
    for dr, dc, T in transforms:
        sr, sc = r0 + dr, c0 + dc
        if sr < 0 or sc < 0 or sr + H > h or sc + W > w:
            continue
        mapping = {}
        ok = True
        for i in range(H):
            for j in range(W):
                v = grid[sr + i][sc + j]
                if v != 0:
                    t = T[i][j]
                    if t in mapping and mapping[t] != v:
                        ok = False
                        break
                    mapping[t] = v
            if not ok:
                break
        if not ok or not mapping:
            continue
        for i in range(H):
            for j in range(W):
                if out[sr + i][sc + j] == 0 and T[i][j] in mapping:
                    out[sr + i][sc + j] = mapping[T[i][j]]
    return out