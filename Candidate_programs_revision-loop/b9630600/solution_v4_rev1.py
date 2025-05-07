from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    q = deque()
    for r in range(H):
        for c in (0, W-1):
            if grid[r][c]==0 and not visited[r][c]:
                visited[r][c]=True; q.append((r,c))
    for c in range(W):
        for r in (0, H-1):
            if grid[r][c]==0 and not visited[r][c]:
                visited[r][c]=True; q.append((r,c))
    while q:
        r,c = q.popleft()
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc = r+dr, c+dc
            if 0<=nr<H and 0<=nc<W and grid[nr][nc]==0 and not visited[nr][nc]:
                visited[nr][nc]=True; q.append((nr,nc))
    out = [row[:] for row in grid]
    for r in range(H):
        for c in range(W):
            if grid[r][c]==0 and not visited[r][c]:
                out[r][c]=3
    return out