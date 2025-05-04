def solve(grid):
    H, W = len(grid), len(grid[0])
    sepR = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    sepC = [c for c in range(W) if all(grid[r][c] == 4 for r in range(H))]
    def intervals(seps, N):
        iv, s = [], 0
        for x in seps + [N]:
            if s < x:
                iv.append((s, x - 1))
            s = x + 1
        return iv
    rows = intervals(sepR, H)
    cols = intervals(sepC, W)
    # template in top‐left block
    br0, bc0 = rows[0], cols[0]
    T = [row[bc0[0]:bc0[1]+1] for row in grid[br0[0]:br0[1]+1]]
    out = [list(row) for row in grid]
    for bi, (r0, r1) in enumerate(rows):
        for bj, (c0, c1) in enumerate(cols):
            if bi == 0 and bj == 0:
                continue
            h, w = r1 - r0 + 1, c1 - c0 + 1
            if h == len(T) and w <= len(T[0]):
                for i in range(h):
                    for j in range(w):
                        if grid[r0+i][c0+j] == 1 and T[i][j] != 4:
                            out[r0+i][c0+j] = T[i][j]
            elif w == len(T[0]) and h <= len(T):
                for i in range(h):
                    for j in range(w):
                        if grid[r0+i][c0+j] == 1 and T[i][j] != 4:
                            out[r0+i][c0+j] = T[i][j]
            elif h == len(T) and w == len(T[0]):
                for i in range(h):
                    for j in range(w):
                        if grid[r0+i][c0+j] == 1 and T[i][j] != 4:
                            out[r0+i][c0+j] = T[i][j]
    return out