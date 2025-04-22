from collections import deque
def solve(grid):
    n,m=len(grid),len(grid[0])
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    res=[row[:] for row in grid]
    def nearest_ref(i,j):
        seen=[[False]*m for _ in range(n)]
        dq=deque([(i,j)])
        seen[i][j]=True
        while dq:
            x,y=dq.popleft()
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and not seen[nx][ny]:
                    seen[nx][ny]=True
                    v=grid[nx][ny]
                    if v in (1,2,7,9):
                        return v
                    dq.append((nx,ny))
        return grid[i][j]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==6:
                res[i][j]=nearest_ref(i,j)
    return res