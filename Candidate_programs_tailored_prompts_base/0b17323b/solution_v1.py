def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    anchors = sorted((i, j) for i in range(h) for j in range(w) if grid[i][j] == 1)
    if len(anchors) < 2:
        return [row[:] for row in grid]
    dr = anchors[1][0] - anchors[0][0]
    dc = anchors[1][1] - anchors[0][1]
    out = [row[:] for row in grid]
    i, j = anchors[-1]
    while True:
        ni, nj = i + dr, j + dc
        if not (0 <= ni < h and 0 <= nj < w):
            break
        out[ni][nj] = 2
        i, j = ni, nj
    return out