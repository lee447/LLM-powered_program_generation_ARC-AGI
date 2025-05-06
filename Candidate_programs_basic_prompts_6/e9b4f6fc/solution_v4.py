def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    best_cc = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]!=0:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                if len(comp) > len(best_cc):
                    best_cc = comp
    rs = [p[0] for p in best_cc]
    cs = [p[1] for p in best_cc]
    r0,r1 = min(rs), max(rs)
    c0,c1 = min(cs), max(cs)
    sub = [row[c0:c1+1] for row in grid[r0:r1+1]]
    H, W = len(sub), len(sub[0])
    # detect border color
    b = None
    cols = set()
    for y in range(W):
        cols.add(sub[0][y]); cols.add(sub[H-1][y])
    for x in range(H):
        cols.add(sub[x][0]); cols.add(sub[x][W-1])
    if len(cols)==1:
        b = cols.pop()
    # remap
    mapping = {}
    nxt = 1
    res = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            v = sub[i][j]
            if b is not None and v == b:
                res[i][j] = b
            else:
                if v == 0 and b is not None:
                    res[i][j] = b
                else:
                    if v not in mapping:
                        mapping[v] = nxt
                        nxt += 1
                    res[i][j] = mapping[v]
    return res