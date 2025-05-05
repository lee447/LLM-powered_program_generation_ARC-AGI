def solve(grid):
    H, W = len(grid), len(grid[0])
    best = []
    for s in (1, -1):
        for start in range(W):
            if grid[1][start] != 0: continue
            seq = []
            for r in range(1, H-1):
                c = start + (r-1)*s
                if 0 <= c < W and grid[r][c] == 0:
                    seq.append((r, c))
                else:
                    break
            if len(seq) >= len(best):
                best = seq
    out = [row[:] for row in grid]
    for r, c in best:
        out[r][c] = 8
    return out