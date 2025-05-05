from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    seen = [[False]*w for _ in range(h)]
    rects: List[Tuple[int,int,int]] = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != border and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                minr, maxr, minc, maxc = i, i, j, j
                while q:
                    x,y = q.popleft()
                    minr, maxr = min(minr,x), max(maxr,x)
                    minc, maxc = min(minc,y), max(maxc,y)
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                width = maxc - minc + 1
                height = maxr - minr + 1
                rects.append((width, height, c))
    rects.sort(key=lambda x: x[0])
    ws = [r[0] for r in rects]
    hs = [r[1] for r in rects]
    cols = ws[-1]
    n = len(rects)
    diffs = [ws[0]] + [ws[i] - ws[i-1] for i in range(1, n)]
    colors = [r[2] for r in rects]
    bands = []
    for i in range(n):
        bands.append((i, diffs[i]))
    height_out = sum(d for _,d in bands)
    out = [[border]*cols for _ in range(height_out)]
    row = 0
    for i, bh in bands:
        for _ in range(bh):
            col = 0
            for j in range(i, n):
                seg = diffs[j]
                color = colors[j]
                for k in range(seg):
                    out[row][col+k] = color
                col += seg
            row += 1
    return out