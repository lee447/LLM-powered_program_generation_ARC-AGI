def solve(grid):
    h, w = len(grid), len(grid[0])
    shape = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 8]
    if not shape: return grid
    mi, mj = min(i for i, j in shape), min(j for i, j in shape)
    rel = [(i - mi, j - mj) for i, j in shape]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            ok = True
            for di, dj in rel:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= h or nj >= w or out[ni][nj] == 8:
                    ok = False
                    break
            if ok:
                for di, dj in rel:
                    out[i + di][j + dj] = 8
    return out