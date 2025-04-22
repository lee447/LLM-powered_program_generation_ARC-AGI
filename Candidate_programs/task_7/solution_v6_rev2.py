import copy

def solve(grid):
    H, W = len(grid), len(grid[0])
    rows_big = [i for i in range(H) if all(grid[i][j] == 4 for j in range(W))]
    cols_big = [j for j in range(W) if all(grid[i][j] == 4 for i in range(H))]
    rcuts = [-1] + rows_big + [H]
    ccuts = [-1] + cols_big + [W]
    blocks = []
    for bi in range(len(rcuts) - 1):
        r0 = rcuts[bi] + 1
        r1 = rcuts[bi + 1] - 1
        if r0 > r1: continue
        for bj in range(len(ccuts) - 1):
            c0 = ccuts[bj] + 1
            c1 = ccuts[bj + 1] - 1
            if c0 > c1: continue
            blocks.append((bi, bj, r0, r1, c0, c1))
    best = None
    bestcnt = -1
    for b in blocks:
        _, _, r0, r1, c0, c1 = b
        cnt = 0
        for i in range(r0, r1 + 1):
            for j in range(c0, c1 + 1):
                if grid[i][j] > 1:
                    cnt += 1
        if cnt > bestcnt:
            bestcnt = cnt
            best = b
    _, _, br0, br1, bc0, bc1 = best
    pattern = []
    for i in range(br0, br1 + 1):
        for j in range(bc0, bc1 + 1):
            v = grid[i][j]
            if v > 1:
                pattern.append((i - br0, j - bc0, v))
    out = copy.deepcopy(grid)
    for b in blocks:
        if b == best: continue
        _, _, r0, r1, c0, c1 = b
        for dr, dc, v in pattern:
            i, j = r0 + dr, c0 + dc
            if 0 <= i < H and 0 <= j < W and out[i][j] == 1:
                out[i][j] = v
    return out