def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    fives = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==5]
    visited = [[False]*w for _ in range(h)]
    clusters = 0
    for i,j in fives:
        if not visited[i][j]:
            clusters += 1
            stack = [(i,j)]
            visited[i][j] = True
            while stack:
                x,y = stack.pop()
                for dx,dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny]==5:
                        visited[nx][ny] = True
                        stack.append((nx,ny))
    endpoints = 0
    for i,j in fives:
        cnt = 0
        for dx,dy in dirs:
            nx, ny = i+dx, j+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny]==5:
                cnt += 1
        if cnt == 1:
            endpoints += 1
    rows = endpoints - (clusters - 1)
    return [[0] for _ in range(rows)]