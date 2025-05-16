from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    marker = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg:
                marker = grid[r][c]
                break
        if marker is not None:
            break
    visited = [[False]*w for _ in range(h)]
    q = deque()
    for r in range(h):
        for c in (0, w-1):
            if grid[r][c] == bg:
                visited[r][c] = True
                q.append((r, c))
    for c in range(w):
        for r in (0, h-1):
            if grid[r][c] == bg and not visited[r][c]:
                visited[r][c] = True
                q.append((r, c))
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == bg:
                visited[nr][nc] = True
                q.append((nr, nc))
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == bg and not visited[r][c]:
                out[r][c] = 2
    return out