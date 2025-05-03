def solve(grid):
    h, w = len(grid), len(grid[0])
    anchors = [i for i in range(min(h, w)) if grid[i][i] == 1]
    step = anchors[1] - anchors[0]
    out = [row[:] for row in grid]
    r = anchors[-1] + step
    while r < min(h, w):
        out[r][r] = 2
        r += step
    return out