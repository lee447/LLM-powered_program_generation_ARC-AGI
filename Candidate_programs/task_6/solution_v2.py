from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for c in row:
            if c != 0:
                counts[c] = counts.get(c, 0) + 1
    block_color = max(counts, key=counts.get)
    visited = [[False]*w for _ in range(h)]
    Ys, Xs = [], []
    block_h = block_w = None
    for y in range(h):
        for x in range(w):
            if grid[y][x] == block_color and not visited[y][x]:
                stack = [(y, x)]
                visited[y][x] = True
                miny = maxy = y
                minx = maxx = x
                while stack:
                    cy, cx = stack.pop()
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == block_color:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                            miny = min(miny, ny)
                            maxy = max(maxy, ny)
                            minx = min(minx, nx)
                            maxx = max(maxx, nx)
                Ys.append(miny)
                Xs.append(minx)
                bh, bw = maxy-miny+1, maxx-minx+1
                if block_h is None:
                    block_h, block_w = bh, bw
    Ys = sorted(set(Ys))
    Xs = sorted(set(Xs))
    sep_rows = []
    for i in range(1, len(Ys)):
        for y in range(Ys[i-1] + block_h, Ys[i]):
            sep_rows.append(y)
    sep_cols = []
    for i in range(1, len(Xs)):
        for x in range(Xs[i-1] + block_w, Xs[i]):
            sep_cols.append(x)
    block_endY = Ys[-1] + block_h - 1
    block_endX = Xs[-1] + block_w - 1
    res = [row[:] for row in grid]
    for y in sep_rows:
        for x in range(w):
            if res[y][x] == 0:
                if Xs[0] <= x <= block_endX:
                    res[y][x] = 2
                else:
                    res[y][x] = 1
    for x in sep_cols:
        for y in range(h):
            if res[y][x] == 0:
                if Ys[0] <= y <= block_endY:
                    res[y][x] = 2
                else:
                    res[y][x] = 1
    return res