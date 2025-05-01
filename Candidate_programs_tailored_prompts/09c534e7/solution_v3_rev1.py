from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != 1:
                q = deque([(i,j)])
                vis[i][j] = True
                comp = [(i,j)]
                touch = (i==0 or i==h-1 or j==0 or j==w-1)
                anchors = []
                if grid[i][j] > 1: anchors.append((i,j))
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny] != 1:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                            if nx==0 or nx==h-1 or ny==0 or ny==w-1: touch = True
                            if grid[nx][ny] > 1: anchors.append((nx,ny))
                if not touch and anchors:
                    cols = {grid[r][c] for r,c in anchors}
                    if len(cols)==1:
                        col = cols.pop()
                        for r,c in comp:
                            out[r][c] = col
    return out