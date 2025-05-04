def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j]!=bg:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                minr, minc = i, j
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c))
                    if r<minr or (r==minr and c<minc):
                        minr, minc = r, c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((minr, minc, col, coords))
    comps.sort(key=lambda x:(x[0],x[1]))
    out = [[bg]*w for _ in range(h)]
    for idx,(_,_,col,coords) in enumerate(comps):
        d = -1 if idx%2==0 else 1
        for r,c in coords:
            out[r][c+d] = col
    return out