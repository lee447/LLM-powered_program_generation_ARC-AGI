from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
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
    dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == bg:
                visited[nr][nc] = True
                q.append((nr, nc))
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == bg and not visited[i][j]:
                out[i][j] = 2
    return out