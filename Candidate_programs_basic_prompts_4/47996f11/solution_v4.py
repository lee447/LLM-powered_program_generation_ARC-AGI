def solve(grid):
    H, W = len(grid), len(grid[0])
    ds = [s for s in range(2, min(H, W) + 1) if H % s == 0 and W % s == 0]
    for s in sorted(ds, reverse=True):
        R, C = H // s, W // s
        patterns = {}
        blocks = {}
        for bi in range(R):
            for bj in range(C):
                blk = tuple(tuple(grid[bi*s + i][bj*s + j] for j in range(s)) for i in range(s))
                blocks[(bi, bj)] = blk
                patterns[blk] = patterns.get(blk, 0) + 1
        singles = [blk for blk, cnt in patterns.items() if cnt == 1]
        if len(singles) == 1 and len(patterns) > 1:
            anomaly = singles[0]
            target = max(patterns.items(), key=lambda x: x[1])[0]
            for (bi, bj), blk in blocks.items():
                if blk == anomaly:
                    for i in range(s):
                        for j in range(s):
                            grid[bi*s + i][bj*s + j] = target[i][j]
            return grid
    return grid