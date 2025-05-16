from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=counts.get)
    fill = 2
    res = [row[:] for row in grid]
    visited = [[False] * w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] == bg and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] == bg and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == bg:
                visited[nx][ny] = True
                q.append((nx, ny))
    for i in range(h):
        for j in range(w):
            if grid[i][j] == bg and not visited[i][j]:
                res[i][j] = fill
    return res