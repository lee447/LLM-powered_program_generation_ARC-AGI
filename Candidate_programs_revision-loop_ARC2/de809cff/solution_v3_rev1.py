from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    orig = [row[:] for row in grid]
    colors = sorted({c for row in orig for c in row if c != 0})
    if len(colors) != 2:
        return [row[:] for row in grid]
    c1, c2 = colors
    visited = [[False]*w for _ in range(h)]
    comp_id = [[-1]*w for _ in range(h)]
    sizes = {}
    cid = 0
    for i in range(h):
        for j in range(w):
            if orig[i][j] == 0 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                comp_id[i][j] = cid
                cnt = 1
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and orig[nx][ny] == 0:
                            visited[nx][ny] = True
                            comp_id[nx][ny] = cid
                            cnt += 1
                            q.append((nx,ny))
                sizes[cid] = cnt
                cid += 1
    if not sizes:
        return [row[:] for row in grid]
    bg_id = max(sizes, key=lambda k: sizes[k])
    new = [row[:] for row in orig]
    holes = [(i,j) for i in range(h) for j in range(w) if orig[i][j] == 0 and comp_id[i][j] != bg_id]
    for i,j in holes:
        new[i][j] = 8
    for i,j in holes:
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = i+dx, j+dy
            if 0 <= ni < h and 0 <= nj < w:
                if orig[ni][nj] == c1:
                    new[ni][nj] = c2
                elif orig[ni][nj] == c2:
                    new[ni][nj] = c1
    return new