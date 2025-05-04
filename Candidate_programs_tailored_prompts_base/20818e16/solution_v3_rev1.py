from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                rmin = i; rmax = i; cmin = j; cmax = j
                while stack:
                    r, c = stack.pop()
                    if r < rmin: rmin = r
                    if r > rmax: rmax = r
                    if c < cmin: cmin = c
                    if c > cmax: cmax = c
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc] == col:
                            visited[rr][cc] = True
                            stack.append((rr, cc))
                height = rmax - rmin + 1
                width = cmax - cmin + 1
                area = height * width
                comps.append((area, height, width, col))
    comps.sort(reverse=True, key=lambda x: x[0])
    h0, w0 = comps[0][1], comps[0][2]
    out = [[comps[0][3]] * w0 for _ in range(h0)]
    for _, hh, ww, col in comps[1:]:
        for i in range(hh):
            if i >= h0: break
            for j in range(ww):
                if j >= w0: break
                out[i][j] = col
    return out