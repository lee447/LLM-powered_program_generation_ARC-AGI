from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and grid[i][j] in (1,8):
                q = deque([(i,j)])
                seen[i][j] = True
                comp = []
                ecount = 0
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    if grid[x][y] == 8:
                        ecount += 1
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] in (1,8):
                            seen[nx][ny] = True
                            q.append((nx,ny))
                if 1 <= ecount <= 2:
                    for x,y in comp:
                        out[x][y] = grid[x][y]
    return out