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
    bg = [[False]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in (0, w-1):
            if orig[i][j] == 0 and not bg[i][j]:
                bg[i][j] = True
                q.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if orig[i][j] == 0 and not bg[i][j]:
                bg[i][j] = True
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and orig[nx][ny] == 0 and not bg[nx][ny]:
                bg[nx][ny] = True
                q.append((nx,ny))
    new = [row[:] for row in orig]
    holes = [(i,j) for i in range(h) for j in range(w) if orig[i][j] == 0 and not bg[i][j]]
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