def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] != bg:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                min_r, min_c = i, j
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    if r<min_r: min_r = r
                    if c<min_c: min_c = c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==color:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append((min_r,min_c,color,cells))
    comps.sort(key=lambda x:(x[0],x[1]))
    new = [[bg]*w for _ in range(h)]
    for idx,(_,_,color,cells) in enumerate(comps):
        dx = -1 if idx%2==0 else 1
        for r,c in cells:
            new[r][c+dx] = color
    return new