def solve(grid):
    h, w = len(grid), len(grid[0])
    ones = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==1]
    visited = [[False]*w for _ in range(h)]
    proto = {}
    for r,c in ones:
        if visited[r][c]: continue
        stack = [(r,c)]
        comp = []
        visited[r][c] = True
        while stack:
            x,y = stack.pop()
            comp.append((x,y))
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==1:
                    visited[nx][ny] = True
                    stack.append((nx,ny))
        rs = [x for x,y in comp]; cs = [y for x,y in comp]
        r0,r1 = min(rs), max(rs)
        c0,c1 = min(cs), max(cs)
        color = grid[r0-1][c0-1]
        corners = {(r0,c0):'tl',(r0,c1):'tr',(r1,c0):'bl',(r1,c1):'br'}
        miss = None
        for pos,tag in corners.items():
            if pos not in comp:
                miss = tag
                break
        proto[color] = miss
    starts = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5:
                starts.append((r,c))
    rs = sorted(set(r for r,c in starts))
    cs = sorted(set(c for r,c in starts))
    out_h = len(rs)*3-1
    out_w = len(cs)*3-1
    out = [[0]*out_w for _ in range(out_h)]
    tpl = {
        'tl':[(0,1),(1,0),(1,1)],
        'tr':[(0,0),(1,0),(1,1)],
        'bl':[(0,0),(0,1),(1,1)],
        'br':[(0,0),(0,1),(1,0)]
    }
    for r,c in starts:
        f = grid[r+1][c+1]
        if f!=5 and f in proto:
            i = rs.index(r)
            j = cs.index(c)
            r0, c0 = i*3, j*3
            for dr,dc in tpl[proto[f]]:
                out[r0+dr][c0+dc] = f
    return out