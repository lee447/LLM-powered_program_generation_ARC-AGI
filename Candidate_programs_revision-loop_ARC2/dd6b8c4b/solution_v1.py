from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    # find center 2
    for i in range(h):
        for j in range(w):
            if g[i][j] == 2:
                cr, cc = i, j
    # detect full enclosure by 6 at distance 2 in four directions
    encl = (
        0 <= cr-2 < h and g[cr-2][cc] == 6 and
        0 <= cr+2 < h and g[cr+2][cc] == 6 and
        0 <= cc-2 < w and g[cr][cc-2] == 6 and
        0 <= cc+2 < w and g[cr][cc+2] == 6
    )
    # partial top fill if 6 above
    top_open = 0 <= cr-2 < h and g[cr-2][cc] == 6
    # partial left fill if 6 left
    left_open = 0 <= cc-2 < w and g[cr][cc-2] == 6
    # fill the 3x3 block around center
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            r, c = cr+di, cc+dj
            if 0 <= r < h and 0 <= c < w:
                if encl:
                    g[r][c] = 9
                else:
                    if top_open and di == -1:
                        g[r][c] = 9
                    if left_open and dj == -1:
                        g[r][c] = 9
    # remove stray 9s between 6 borders on each row
    for i in range(h):
        pos = [j for j in range(w) if g[i][j] == 6]
        if len(pos) >= 2:
            l, r = min(pos), max(pos)
            for j in range(l+1, r):
                if grid[i][j] == 9 and g[i][j] == 9:
                    g[i][j] = 7
    return g