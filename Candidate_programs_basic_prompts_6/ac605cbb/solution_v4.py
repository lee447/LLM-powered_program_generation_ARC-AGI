def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if len(pts) == 1:
        r, c, col = pts[0]
        ax = (h - 1) // 2
        r2 = 2 * ax - r
        out = [row[:] for row in grid]
        dr = 1 if r2 > r else -1
        for y in range(r, r2 + dr, dr):
            out[y][c] = col if y == r or y == r2 else 5
        return out
    pts.sort()
    out = [[0]*w for _ in range(h)]
    for r,c,col in pts:
        out[r][c] = col
    for i in range(len(pts)-1):
        r1,c1,col1 = pts[i]
        r2,c2,col2 = pts[i+1]
        dR = r2 - r1
        dC = c2 - c1
        # vertical
        step = 1 if dR>0 else -1
        for y in range(r1, r2+step, step):
            if out[y][c1] == 0:
                out[y][c1] = col1 if y==r1 or y==r2 else 5
        # horizontal
        step = 1 if dC>0 else -1
        for x in range(c1, c1+dC+step, step):
            if out[r2][x] == 0:
                out[r2][x] = col2 if x==c1 or x==c2 else 5
    # diagonal from last intersection if new color
    if len(pts) >= 2:
        r1,c1,_ = pts[0]
        r2,c2,_ = pts[1]
        ix, iy = r2, c1
        col = out[ix][iy]
        if col != 0 and col != pts[0][2] and col != pts[1][2]:
            y, x = ix, iy
            while 0 <= y < h and 0 <= x < w:
                out[y][x] = col
                y += 1
                x -= 1
    return out