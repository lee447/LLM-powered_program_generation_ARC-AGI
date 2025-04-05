from collections import deque
def solve(grid):
    if not grid or not grid[0]:
        return grid
    h, w = len(grid), len(grid[0])
    key = {9, 6, 7, 4}
    visited = [[False]*w for _ in range(h)]
    best = None
    best_count = 0
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and grid[r][c] in key:
                q = deque([(r, c)])
                visited[r][c] = True
                comp = []
                while q:
                    rr, cc = q.popleft()
                    comp.append((rr, cc))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] in key:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                if len(comp) > best_count:
                    best_count = len(comp)
                    minr = min(rp for rp, cp in comp)
                    maxr = max(rp for rp, cp in comp)
                    minc = min(cp for rp, cp in comp)
                    maxc = max(cp for rp, cp in comp)
                    best = (minr, maxr, minc, maxc)
    if best is None:
        return grid
    minr, maxr, minc, maxc = best
    if maxr - minr < 2 or maxc - minc < 2:
        return []
    return [row[minc+1:maxc] for row in grid[minr+1:maxr]]