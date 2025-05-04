def solve(grid):
    H = len(grid)
    W = len(grid[0])
    base = grid[H-1][0]
    hole_row = H-2
    holes = []
    c = 0
    while c < W:
        if grid[hole_row][c] == 0:
            start = c
            while c < W and grid[hole_row][c] == 0:
                c += 1
            holes.append((start, c - start))
        else:
            c += 1
    visited = [[False]*W for _ in range(H)]
    shapes = []
    for r in range(hole_row):
        for c in range(W):
            if grid[r][c] not in (0, base) and not visited[r][c]:
                col = grid[r][c]
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<hole_row and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                h = r1-r0+1
                w = c1-c0+1
                shapes.append({'h':h, 'w':w, 'col':col})
    new = [row[:] for row in grid]
    for r in range(hole_row):
        for c in range(W):
            new[r][c] = 0
    used = [False]*len(shapes)
    for start,len0 in holes:
        idx = -1; rot = False
        for i,sh in enumerate(shapes):
            if not used[i] and sh['w']==len0:
                idx = i; rot = False; break
        if idx<0:
            for i,sh in enumerate(shapes):
                if not used[i] and sh['h']==len0:
                    idx = i; rot = True; break
        sh = shapes[idx]
        used[idx] = True
        if not rot:
            h, w = sh['h'], sh['w']
        else:
            h, w = sh['w'], sh['h']
        r0 = hole_row - h + 1
        for dr in range(h):
            for dc in range(w):
                new[r0+dr][start+dc] = sh['col']
    return new