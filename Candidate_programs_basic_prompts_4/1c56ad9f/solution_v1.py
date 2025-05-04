def solve(grid):
    h = len(grid)
    w = len(grid[0])
    cols = set(x for y in range(h) for x in range(w) if grid[y][x] != 0 and ((y>0 and grid[y-1][x]==grid[y][x]) or (y<h-1 and grid[y+1][x]==grid[y][x])))
    rows = set(y for y in range(h) for x in range(w) if grid[y][x] != 0 and ((x>0 and grid[y][x-1]==grid[y][x]) or (x<w-1 and grid[y][x+1]==grid[y][x])))
    if not rows or not cols:
        return grid
    ry = sorted(rows)
    rx = sorted(cols)
    dy = ry[1]-ry[0] if len(ry)>1 else h
    dx = rx[1]-rx[0] if len(rx)>1 else w
    out = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c==0: continue
            if x in cols and ((y>0 and grid[y-1][x]==c) or (y<h-1 and grid[y+1][x]==c)):
                i = y - (ry[0]+1)
                off = round(-((i+1)% (2*dy) == dy//2) + ((i+1)% (2*dy) == 3*dy//2))
                nx = x + off
                out[y][nx] = c
            elif y in rows and ((x>0 and grid[y][x-1]==c) or (x<w-1 and grid[y][x+1]==c)):
                j = x - (rx[0]+1)
                off = round(-((j+1)% (2*dx) == dx//2) + ((j+1)% (2*dx) == 3*dx//2))
                ny = y + off
                out[ny][x] = c
            else:
                out[y][x] = c
    return out