from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = [(i,j)]
                for x,y in stack:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                comps.append(comp)
    comp = max(comps, key=len)
    rs = [p[0] for p in comp]; cs = [p[1] for p in comp]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    hh, ww = r1-r0+1, c1-c0+1
    A = [row[c0:c1+1] for row in grid[r0:r0+hh]]
    out = [row[:] for row in grid]
    def f_h(r,c): return A[r][ww-1-c]
    def f_v(r,c): return A[hh-1-r][c]
    def f_b(r,c): return A[hh-1-r][ww-1-c]
    for dr,dc,f in ((0,1,f_h),(1,0,f_v),(1,1,f_b)):
        bi = r0 + dr*hh
        bj = c0 + dc*ww
        mapping = {}
        for r in range(hh):
            for c in range(ww):
                i, j = bi+r, bj+c
                if 0 <= i < h and 0 <= j < w and grid[i][j] != 0:
                    mapping[f(r,c)] = grid[i][j]
        for r in range(hh):
            for c in range(ww):
                i, j = bi+r, bj+c
                if 0 <= i < h and 0 <= j < w:
                    out[i][j] = mapping.get(f(r,c), 0)
    return out