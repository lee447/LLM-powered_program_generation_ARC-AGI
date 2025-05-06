def solve(grid):
    R, C = len(grid), len(grid[0])
    dirs = [(1, 1), (1, -1)]
    best = []
    for dr, dc in dirs:
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    pr, pc = r - dr, c - dc
                    if not (0 <= pr < R and 0 <= pc < C and grid[pr][pc] == 0):
                        seq = []
                        nr, nc = r, c
                        while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                            seq.append((nr, nc))
                            nr += dr
                            nc += dc
                        if len(seq) > len(best):
                            best = seq
    out = [row[:] for row in grid]
    for r, c in best:
        out[r][c] = 8
    return out