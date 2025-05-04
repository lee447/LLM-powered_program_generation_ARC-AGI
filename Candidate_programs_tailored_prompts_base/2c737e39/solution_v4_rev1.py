from collections import deque

def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    def has_neighbor_color(r, c):
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] not in (0, 5):
                return True
        return False
    if has_neighbor_color(*greys[0]):
        src, tgt = greys[0], greys[1]
    else:
        src, tgt = greys[1], greys[0]
    queue = deque()
    visited = set()
    for dr, dc in dirs:
        nr, nc = src[0] + dr, src[1] + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] not in (0, 5):
            queue.append((nr, nc))
            visited.add((nr, nc))
    cluster = []
    while queue:
        r, c = queue.popleft()
        cluster.append((r, c, grid[r][c]))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in visited and grid[nr][nc] not in (0, 5):
                visited.add((nr, nc))
                queue.append((nr, nc))
    dy = tgt[0] - src[0]
    dx = tgt[1] - src[1]
    out = [row[:] for row in grid]
    out[tgt[0]][tgt[1]] = 0
    for r, c, v in cluster:
        nr, nc = r + dy, c + dx
        if 0 <= nr < h and 0 <= nc < w:
            out[nr][nc] = v
    return out