def solve(grid):
    H, W = len(grid), len(grid[0])
    pts2 = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 2]
    if not pts2:
        return grid
    minr = min(i for i, _ in pts2)
    maxr = max(i for i, _ in pts2)
    minc = min(j for _, j in pts2)
    maxc = max(j for _, j in pts2)
    sh = maxr - minr + 1
    sw = maxc - minc + 1
    shape = [[1 if grid[minr + i][minc + j] == 2 else 0 for j in range(sw)] for i in range(sh)]
    out = [row[:] for row in grid]
    fours = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 4]
    for r1, c1 in fours:
        r2 = r1 + sh + 1
        c2 = c1 + sw + 1
        if r2 < H and c2 < W:
            if grid[r1][c2] == 4 and grid[r2][c1] == 4 and grid[r2][c2] == 4:
                for i in range(sh):
                    for j in range(sw):
                        if shape[i][j]:
                            out[r1 + 1 + i][c1 + 1 + j] = 2
    return out