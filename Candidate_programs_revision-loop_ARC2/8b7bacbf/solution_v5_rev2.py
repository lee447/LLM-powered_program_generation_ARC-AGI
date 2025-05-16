from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    ring_colors = set()
    holes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                comp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]==0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                neigh = set()
                for x,y in comp:
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]!=0:
                            neigh.add(grid[nx][ny])
                if len(neigh)==1:
                    c = next(iter(neigh))
                    ring_colors.add(c)
                    holes.append(comp)
    if ring_colors:
        new_color = max(ring_colors) + 2
        for comp in holes:
            for x,y in comp:
                out[x][y] = new_color
    return out