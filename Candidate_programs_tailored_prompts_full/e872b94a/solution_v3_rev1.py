from collections import deque
def solve(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==5 and not visited[i][j]:
                comps+=1
                q=deque([(i,j)])
                visited[i][j]=True
                while q:
                    x,y=q.popleft()
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==5:
                            visited[nx][ny]=True
                            q.append((nx,ny))
    res = comps+1
    return [[0] for _ in range(res)]