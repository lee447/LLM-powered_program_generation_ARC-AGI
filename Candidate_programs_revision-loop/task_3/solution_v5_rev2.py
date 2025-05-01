from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False] * w for _ in range(h)]
    shapes = []
    mapping = {}
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                seed = None
                while stack:
                    y, x = stack.pop()
                    cells.append((y, x))
                    if grid[y][x] != 1:
                        seed = (y, x, grid[y][x])
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] != 0:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                ys = [y for y, x in cells]
                xs = [x for y, x in cells]
                miny, minx = min(ys), min(xs)
                sig = tuple(sorted(((y - miny, x - minx) for y, x in cells)))
                if seed:
                    sy, sx, v = seed
                    mapping[sig] = (sy - miny, sx - minx, v)
                shapes.append((sig, miny, minx))
    out = [row[:] for row in grid]
    for sig, miny, minx in shapes:
        if sig in mapping:
            oy, ox, v = mapping[sig]
            y, x = miny + oy, minx + ox
            if out[y][x] == 1:
                out[y][x] = v
    return out