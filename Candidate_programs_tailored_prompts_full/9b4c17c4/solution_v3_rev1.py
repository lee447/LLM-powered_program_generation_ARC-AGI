from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # detect seam orientation and index
    vertical = False
    seam = None
    for r in range(h):
        for c in range(w-1):
            if {grid[r][c], grid[r][c+1]} == {1, 8}:
                vertical = True
                seam = c
                break
        if seam is not None:
            break
    if not vertical:
        for r in range(h-1):
            for c in range(w):
                if {grid[r][c], grid[r+1][c]} == {1, 8}:
                    seam = r
                    break
            if seam is not None:
                break
    # find all red connected components
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2 and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == 2:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                comps.append(comp)
    out = [row[:] for row in grid]
    # remove originals
    for comp in comps:
        r0, c0 = comp[0]
        if vertical:
            bg = 1 if c0 <= seam else 8
        else:
            bg = 1 if r0 <= seam else 8
        for r,c in comp:
            out[r][c] = bg
    # reflect
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        hblk = maxr - minr + 1
        wblk = maxc - minc + 1
        if vertical:
            side = 'L' if minc <= seam else 'R'
            if side == 'L':
                new_min_c = seam+1 + (seam - maxc)
            else:
                new_min_c = seam - (minc - (seam+1))
            for r,c in comp:
                nc = new_min_c + (c - minc)
                out[r][nc] = 2
        else:
            side = 'T' if minr <= seam else 'B'
            if side == 'T':
                new_min_r = seam+1 + (seam - maxr)
            else:
                new_min_r = seam - (minr - (seam+1))
            for r,c in comp:
                nr = new_min_r + (r - minr)
                out[nr][c] = 2
    return out