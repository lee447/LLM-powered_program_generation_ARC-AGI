from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs8 = [(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if not (dx==0 and dy==0)]
    visited = [[False]*W for _ in range(H)]
    regions = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==1 and not visited[i][j]:
                comp = []
                dq = deque([(i,j)])
                visited[i][j] = True
                while dq:
                    x,y = dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs4:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny] = True
                            dq.append((nx,ny))
                regions.append(comp)
    if not regions:
        return grid
    M = set(max(regions, key=len))
    out = [row[:] for row in grid]
    for x,y in M:
        for dx,dy in dirs8:
            nx,ny = x+dx, y+dy
            if 0<=nx<H and 0<=ny<W and (nx,ny) not in M:
                out[nx][ny] = 2
    nonM = [(i,j) for i in range(H) for j in range(W) if (i,j) not in M]
    for x,y in M:
        mind = min(max(abs(x-i),abs(y-j)) for i,j in nonM)
        if mind==1:
            out[x][y] = 8
        elif mind==2:
            out[x][y] = 6
    return out