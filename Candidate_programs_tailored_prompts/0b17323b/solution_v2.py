def solve(grid):
    n = len(grid)
    m = len(grid[0]) if grid else 0
    anchors = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
    if len(anchors) < 2:
        return grid
    anchors.sort(key=lambda x: (x[0], x[1]))
    (r0, c0), (r1, c1) = anchors[0], anchors[1]
    dr = r1 - r0
    dc = c1 - c0
    if abs(dr) >= abs(dc):
        anchors.sort(key=lambda x: x[0], reverse=(dr < 0))
    else:
        anchors.sort(key=lambda x: x[1], reverse=(dc < 0))
    r, c = anchors[-1]
    while True:
        r += dr
        c += dc
        if not (0 <= r < n and 0 <= c < m):
            break
        grid[r][c] = 2
    return grid