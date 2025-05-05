def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                clusters.append(comp)
    clusters.sort(key=lambda comp: (min(r for r,c in comp), min(c for r,c in comp)))
    comp = clusters[0]
    min_r = min(r for r,c in comp)
    max_r = max(r for r,c in comp)
    min_c = min(c for r,c in comp)
    max_c = max(c for r,c in comp)
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    out = [[0]*W for _ in range(H)]
    for r,c in comp:
        out[r-min_r][c-min_c] = grid[r][c]
    return out