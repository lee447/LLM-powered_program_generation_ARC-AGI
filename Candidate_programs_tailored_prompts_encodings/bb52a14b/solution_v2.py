def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    verts = []
    hors = []
    for i in range(h):
        for j in range(w):
            if i + 2 < h and grid[i][j] == 1 and grid[i+1][j] == 4 and grid[i+2][j] == 1:
                verts.append((i, j))
            if j + 2 < w and grid[i][j] == 4 and grid[i][j+1] == 8 and grid[i][j+2] == 4:
                hors.append((i, j))
    for r, c in verts:
        pat = [1, 4, 1]
        for rr in range(r-1, -1, -1):
            if grid[rr][c] == 8: break
            if out[rr][c] == 0:
                out[rr][c] = pat[(rr - r) % 3]
        for rr in range(r+3, h):
            if grid[rr][c] == 8: break
            if out[rr][c] == 0:
                out[rr][c] = pat[(rr - r) % 3]
    for r, c in hors:
        pat = [4, 8, 4]
        for cc in range(c-1, -1, -1):
            if grid[r][cc] == 8: break
            if out[r][cc] == 0:
                out[r][cc] = pat[(cc - c) % 3]
        for cc in range(c+3, w):
            if grid[r][cc] == 8: break
            if out[r][cc] == 0:
                out[r][cc] = pat[(cc - c) % 3]
    return out