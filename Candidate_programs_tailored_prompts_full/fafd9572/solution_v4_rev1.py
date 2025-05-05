from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    modules = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1 and not visited[r][c]:
                comp = []
                dq = deque([(r, c)])
                visited[r][c] = True
                while dq:
                    x, y = dq.popleft()
                    comp.append((x, y))
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            if dx == 0 and dy == 0:
                                continue
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
                                visited[nx][ny] = True
                                dq.append((nx, ny))
                top = min(comp)
                modules.append((top, comp))
    modules.sort(key=lambda x: x[0])
    anchors = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] > 1]
    anchors.sort(key=lambda x: (x[0], x[1]))
    vals = [v for _, _, v in anchors]
    out = [row[:] for row in grid]
    for (_, comp), v in zip(modules, vals):
        for x, y in comp:
            out[x][y] = v
    return out