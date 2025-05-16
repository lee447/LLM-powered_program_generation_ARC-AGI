import collections
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    cnt = collections.Counter(x for row in grid for x in row)
    cols = [c for c in range(m) if len({grid[r][c] for r in range(n)}) == 1]
    stripe_col = min(cols, key=lambda c: cnt[grid[0][c]])
    stripe_color = grid[0][stripe_col]
    stripe_row = next(r for r in range(n) if sum(1 for c in range(m) if grid[r][c] == stripe_color) > 1)
    r1, r2 = 0, stripe_row - 1
    r3, r4 = stripe_row + 1, n - 1
    c1, c2 = 0, stripe_col - 1
    c3, c4 = stripe_col + 1, m - 1
    out = [[0] * m for _ in range(n)]
    for r in range(n):
        out[r][stripe_col] = stripe_color
    for c in range(m):
        out[stripe_row][c] = stripe_color
    def region(r0, r1, c0, c1):
        return [grid[r][c0:c1+1] for r in range(r0, r1+1)]
    def write_region(r0, c0, reg):
        for i in range(len(reg)):
            for j in range(len(reg[0])):
                out[r0 + i][c0 + j] = reg[i][j]
    def mirror_h(g):
        return [row[::-1] for row in g]
    def mirror_v(g):
        return g[::-1]
    def rot180(g):
        return mirror_v(mirror_h(g))
    quads = [
        (r1, c1, region(r1, r2, c1, c2), lambda g: g, lambda g: g),
        (r1, c3, region(r1, r2, c3, c4), mirror_h, mirror_h),
        (r3, c1, region(r3, r4, c1, c2), mirror_v, mirror_v),
        (r3, c3, region(r3, r4, c3, c4), rot180, rot180)
    ]
    for r0, c0, R, trans, inv in quads:
        if not R or not R[0]:
            continue
        G = trans(R)
        cnt2 = collections.Counter(x for row in G for x in row)
        b = cnt2.most_common(1)[0][0]
        h, w = len(G), len(G[0])
        anchors = []
        for i in range(min(h, w)):
            v = G[i][i]
            if v != b:
                anchors.append(v)
            else:
                break
        if not anchors:
            anchors = [b]
        Gout = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                layer = min(i, j, h - 1 - i, w - 1 - j)
                Gout[i][j] = anchors[layer % len(anchors)]
        F = inv(Gout)
        write_region(r0, c0, F)
    return out