from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    for i in range(R):
        if any(grid[i][j] != 0 for j in range(C)):
            r0 = i
            break
    for j in range(C):
        if grid[r0][j] != 0:
            c0 = j
            break
    w = 0
    while c0 + w < C and grid[r0][c0 + w] != 0:
        w += 1
    h = 0
    while r0 + h < R and grid[r0 + h][c0] != 0:
        h += 1
    P = [grid[r0 + i][c0 : c0 + w] for i in range(h)]
    def mirror_h(M): return [row[::-1] for row in M]
    def mirror_v(M): return M[::-1]
    def rot180(M): return [row[::-1] for row in M[::-1]]
    fns = [lambda M: M, mirror_h, mirror_v, rot180]
    uvals = {v for row in P for v in row if v != 0}
    out = [[0] * C for _ in range(R)]
    for qi, (dr, dc) in enumerate([(0, 0), (0, w), (h, 0), (h, w)]):
        pat = fns[qi](P)
        mapping = {}
        for i in range(h):
            for j in range(w):
                gr, gc = r0 + dr + i, c0 + dc + j
                if 0 <= gr < R and 0 <= gc < C:
                    v = grid[gr][gc]
                    if v != 0 and pat[i][j] != 0:
                        mapping[pat[i][j]] = v
        for t in uvals:
            mapping.setdefault(t, 0)
        for i in range(h):
            for j in range(w):
                t = pat[i][j]
                if t != 0:
                    out[r0 + dr + i][c0 + dc + j] = mapping[t]
    return out