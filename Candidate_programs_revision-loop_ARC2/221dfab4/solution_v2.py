def solve(grid):
    h, w = len(grid), len(grid[0])
    cnt = {}
    for r in grid:
        for c in r:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=lambda x: cnt[x])
    shape = max((k for k in cnt if k != bg), key=lambda x: cnt[x])
    pts = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==shape]
    rs = [i for i,_ in pts]; cs = [j for _,j in pts]
    r0, r2 = min(rs), max(rs); c0, c2 = min(cs), max(cs)
    r1 = (r0 + r2)//2; c1 = (c0 + c2)//2
    out = [row[:] for row in grid]
    for i,j in pts:
        out[i][j] = bg
    def hor(y):
        for x in range(c0, c2+1):
            out[y][x] = 3
    def ver(x, y_start, y_end):
        for y in range(y_start, y_end+1):
            out[y][x] = 4
    hor(r0)
    hor(r1)
    hor(r2)
    # detect which vertical segments exist
    upper_left = any(grid[r][c0] == shape for r in range(r0, r1+1))
    upper_right = any(grid[r][c2] == shape for r in range(r0, r1+1))
    lower_left = any(grid[r][c0] == shape for r in range(r1, r2+1))
    lower_right = any(grid[r][c2] == shape for r in range(r1, r2+1))
    if upper_left: ver(c0, r0, r1)
    if upper_right: ver(c2, r0, r1)
    if lower_left: ver(c0, r1, r2)
    if lower_right: ver(c2, r1, r2)
    return out