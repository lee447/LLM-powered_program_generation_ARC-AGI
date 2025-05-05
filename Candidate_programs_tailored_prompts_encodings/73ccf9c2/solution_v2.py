def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                minr = min(r for r,c in cells)
                minc = min(c for r,c in cells)
                maxr = max(r for r,c in cells)
                maxc = max(c for r,c in cells)
                clusters.append((minr,minc,maxr,maxc,col,cells))
    clusters.sort(key=lambda x: (x[0],x[1]))
    minr,minc,maxr,maxc,col,cells = clusters[0]
    out_h = maxr - minr + 1
    out_w = maxc - minc + 1
    out = [[0]*out_w for _ in range(out_h)]
    for r,c in cells:
        out[r-minr][c-minc] = col
    return out