import numpy as np
from collections import deque, defaultdict

def solve(grid):
    H, W = len(grid), len(grid[0])
    M = [[cell if cell != 2 else 0 for cell in row] for row in grid]
    visited = [[False]*W for _ in range(H)]
    shapes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] not in (0,2) and not visited[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs = [r for r,_ in cells]
                cs = [cc for _,cc in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                cr = (r0 + r1)//2
                cc = (c0 + c1)//2
                shapes.append((c, cr, cc))
    for _, cr, cc in shapes:
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            r, c = cr+dr, cc+dc
            while 0 <= r < H and 0 <= c < W:
                if grid[r][c] not in (0,2):
                    break
                if M[r][c] == 0:
                    M[r][c] = 2
                r += dr; c += dc
    return M