def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j]=True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c,col))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]!=0:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    lines = []
    cluster = None
    for comp in comps:
        pts = comp
        rs = [p[0] for p in pts]
        cs = [p[1] for p in pts]
        if len(pts)>=3 and (min(rs)==max(rs) or min(cs)==max(cs)):
            lines.append((len(pts), pts[0][2]))
        else:
            cluster = (len(pts), pts[0][2])
    lines.sort(reverse=True, key=lambda x:x[0])
    L = len(lines)
    csize, ccol = cluster
    N = csize + 2*L
    out = [[0]*N for _ in range(N)]
    for layer in range(L):
        color = lines[layer][1]
        for i in range(N):
            out[layer][i] = color
            out[N-1-layer][i] = color
            out[i][layer] = color
            out[i][N-1-layer] = color
    for dr in range(csize):
        for dc in range(csize):
            out[L+dr][L+dc] = ccol
    return out