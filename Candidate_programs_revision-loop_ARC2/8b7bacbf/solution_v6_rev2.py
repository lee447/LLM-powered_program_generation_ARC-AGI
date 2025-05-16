from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    holes = []
    border_colors = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                cells = [(i, j)]
                touch_edge = False
                nb = set()
                while q:
                    x, y = q.popleft()
                    if x == 0 or x == h-1 or y == 0 or y == w-1:
                        touch_edge = True
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w:
                            v = grid[nx][ny]
                            if v == 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                cells.append((nx, ny))
                            elif v != 0:
                                nb.add(v)
                if not touch_edge and len(nb) == 1:
                    holes.append(cells)
                    border_colors.add(next(iter(nb)))
    if border_colors:
        D = min(border_colors) + max(border_colors)
        for cells in holes:
            for x, y in cells:
                grid[x][y] = D
    return grid