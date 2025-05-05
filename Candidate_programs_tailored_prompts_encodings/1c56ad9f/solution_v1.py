def solve(grid):
    H, W = len(grid), len(grid[0])
    result = [[0]*W for _ in range(H)]
    pts = {(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0}
    if not pts:
        return result
    color = next(grid[r][c] for r, c in pts if grid[r][c] != 0)
    h_rows = sorted({r for r, c in pts if c+1<W and grid[r][c]==grid[r][c+1]})
    inner = h_rows[1:-1]
    target = None
    if inner:
        target = inner[len(inner)//2]
    for y in h_rows:
        dx = 1 if y==target else 0
        for c in range(W):
            if (y, c) in pts:
                nc = c+dx
                if 0<=nc<W:
                    result[y][nc] = color
    v_cols = sorted({c for r, c in pts if r+1<H and grid[r][c]==grid[r+1][c]})
    if len(inner)==1:
        for x in v_cols:
            for i in range(len(h_rows)-1):
                y0, y1 = h_rows[i]+1, h_rows[i+1]-1
                dx = -1 if i==0 else 0
                for y in range(y0, y1+1):
                    if (y, x) in pts:
                        nx = x+dx
                        if 0<=nx<W:
                            result[y][nx] = color
    else:
        for x in v_cols:
            for r, c in pts:
                if c==x and not (r in h_rows):
                    result[r][c] = color
    return result