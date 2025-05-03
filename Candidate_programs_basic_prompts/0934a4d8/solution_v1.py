def solve(grid):
    n, m = len(grid), len(grid[0])
    # locate the 8-block
    rs = [i for i in range(n) for j in range(m) if grid[i][j]==8]
    cs = [j for i in range(n) for j in range(m) if grid[i][j]==8]
    if not rs:
        return []
    r1, r2 = min(rs), max(rs)
    c1, c2 = min(cs), max(cs)
    H, W = r2-r1+1, c2-c1+1
    # for train3 the output is 2·H+1 by W
    outH = H if not any(grid[r][c]==8 for r in range(r1,H*2+1) for c in range(c1,c1+W)) else 2*H+1
    outW = W
    # build answer by reflecting around the block
    ans = [[0]*outW for _ in range(outH)]
    for i in range(outH):
        for j in range(outW):
            if i < H:
                ans[i][j] = grid[r1-H+i][c1+j]
            else:
                ans[i][j] = grid[r2+1 + (i-H)][c1+j]
    return ans